### 项目需求

评论的爬取

爬取地址：`https://item.jd.com/12398725.html`

### 获取评论地址

随便复制一个评论者的名字搜索。

首先源代码中搜索，搜索不到。

考虑在加载数据中，到开发者工具的网络中搜索。

找到评论地址

> https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=12398725&score=0&sortType=5&page=1&pageSize=10&isShadowSku=0&rid=0&fold=1

- 里面的重要参数：
  - `productId`：代表每个商品
  - `page`:代表页码
  - `pageSize`: 代表每页多少条评论

### 创建项目

- scrapy startproject jd_comment
- cd jd_comment

- scrapy  genspider jd jd.com

### 代码实现

- 修改配置文件`setting.py`:

  - 设置请求头

    ```python
    # Crawl responsibly by identifying yourself (and your website) on the user-agent
    USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.37'
    
    ```

  - robots协议

    - 默认遵守robots协议

    ```python
    # Obey robots.txt rules
    ROBOTSTXT_OBEY = False
    ```

  - 开启pipelines

    - 用于保存数据到数据库

    ```python
    # Configure item pipelines
    # See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
    ITEM_PIPELINES = {
        'jd_comment.pipelines.JdCommentPipeline': 300,
    }
    ```

- 修改spiders文件夹下面的

  - `jd.py`

```python
# -*- coding: utf-8 -*-
import scrapy
import json
import re

class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=12398725&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&rid=0&fold=1']   
    page = 0   # 标记评论页码

    def parse(self, response):
        # 转成字典格式
        re_t = re.findall(r'fetchJSON_comment98\((.*)\);', response.text)[0]
        json_t = json.loads(re_t)
        
        coment_list = json_t['comments']
        for comment in coment_list:
            id = comment['id']   # 评论者id
            content = comment['content']   # 评论
            creationTime = comment['creationTime']   # 评论时间
            yield {'_id':id, 'content':content, 'creationTime':creationTime}
        
        self.page += 1
        if self.page < 20:
        	# 下一页
            next_url = f'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=12398725&score=0&sortType=5&page={self.page}&pageSize=10&isShadowSku=0&rid=0&fold=1'
            yield scrapy.Request(next_url)

```

修改start_urls

```python
 start_urls = ['https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=12398725&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&rid=0&fold=1'] 
```

定义一个page参数标记页码， 每爬取一页page加一

```python
page = 0
```

```python
self.page += 1
```

下一页爬取，callback默认是parse函数

```python
yield scrapy.Request(next_url)
```

当然也可以不用在parse函数中处理下一页地址，start_urls是一个列表，只需用列表推导式把评论地址都添加到starts_urls中即可

```python
 start_urls = [f'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=12398725&score=0&sortType=5&page={page}&pageSize=10&isShadowSku=0&rid=0&fold=1' for page in range(20) ] 
```

- 修改`pipelines.py`文件

  ```python
  from pymongo import MongoClient
  
  class JdCommentPipeline(object):
      
      def open_spider(self, spider):
          self.client = MongoClient(host='localhost', port=27017)
          self.db = self.client['scrapy_data']['JdComment']
          
      def close_spider(self, spider):
          self.client.close()
      
      def process_item(self, item, spider):
          print(item)
          self.db.insert_one(item)
          return item
  ```

  `open_spider`: 数据库连接

  `close_spider`: 数据库关闭

  `process_item`: 保存数据到数据库中