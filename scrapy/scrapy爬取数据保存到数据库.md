## scrapy保存数据到数据库中

### 页面解析函数（默认为parse函数）

```python
# -*- coding: utf-8 -*-
import scrapy

class JdSpider(scrapy.Spider):
    ···
    def parse(self, response):
        pass
```

在这个函数中我们可以通过yield返回：

- 一个Request对象：处理完一个页面后我们可能要处理别的页面，这个时候我们就可以返回一个Request对象。

- 封装的数据（item或字典）：在获取数据可以把数据封装（item或字典）后返回。

### 返回封装的数据

```python
# -*- coding: utf-8 -*-
import scrapy
class DbSpider(scrapy.Spider):
    ...
    def parse(self, response):
        book_list = response.xpath('//ul[@class="subject-list"]/li')
        for book in book_list:
            # 获取书名
            name = book.xpath('.//h2/a/@title').get()
            # 获取作者、出版社、出版日期、价格
            pub = book.xpath('.//div[@class="pub"]/text()').get().strip()
            # 评分
            rating_nums = book.xpath('.//span[@class="rating_nums"]/text()').get()
            # 返回字典对象
            yield {
                'name':name,
                'pub':pub,
                'rating_nums':rating_nums
            }
        ...
```

在前面我们已经爬取到数据了

```python
 yield {'name':name,'pub':pub,'rating_nums':rating_nums}
```

在这里我们`yield`了一个字典对象.

在创建一个Scrapy项目时，会自动生成一个pipelines.py文件，在pipelines.py下我们可以获取到我们封装的数据。

### 启用pipelines

`在配置文件settings.py中。`

```python
# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'douban_book.pipelines.DoubanBookPipeline': 300,
}
```

pipelines.py

```python
class DoubanBookPipeline(object):
    def process_item(self, item, spider):
        return item
```

`process_item`:用来处理每一项由Spider爬取到的数据

`item` : 取到的一项数据（Item或字典）,就是我们返回的封装对象。

`spider` : 爬取此项数据的Spider对象。

### 数据入库

```python
from pymongo import MongoClient

class DoubanBookPipeline(object):
    def open_spider(self, spider):
        '''连接数据库'''
        self.client = MongoClient(host='localhost', port=27017)
        self.db = self.client['scrapy_data'][f'{spider.name}']
        
    def close_spider(self, spider):
        '''关闭数据库'''
        self.client.close()
    
    def process_item(self, item, spider):
        '''保存数据到数据库中'''
        self.db.insert_one(item)
        return item
```

`open_spider `：Spider打开时（处理数据前）回调该方法，通常该方法用于在开始处理数据之前完成某些初始化工作，如连接数据库。

`close_spider` :  Spider关闭时（处理数据后）回调该方法，通常该方法用于在处理完所有数据之后完成某些清理工作，如关闭数据库。