### 项目需求

爬取豆瓣图书编程类按评价排序的图书信息

地址： [https://book.douban.com/tag/%E7%BC%96%E7%A8%8B?type=S](https://book.douban.com/tag/编程?type=S)

爬取数据：书名，作者，评分。

### 创建scrapy项目

在命令行中输入

> scrapy startproject douban_book

在命令行中进入创建好的项目创建爬虫文件，当然可以自己创建。

> cd douban_book
>
> scrapy genspider db douban.com

在douban_book.spiders下面就创建了一个名为db.py的爬虫文件

文件内容：

```python
# -*- coding: utf-8 -*-
import scrapy


class DbSpider(scrapy.Spider):
    # 爬虫名，可以用于启动爬虫
    name = 'db'   
    # 爬虫爬取的域名，在别的域名下爬取不了
    allowed_domains = ['douban.com']   
    # 爬虫开始位置
    start_urls = ['http://douban.com/']   

    # 默认的解析页面函数
    def parse(self, response):
        pass
```

更改`start_urls`，即爬虫起始的位置。

```python
start_urls = ['https://book.douban.com/tag/%E7%BC%96%E7%A8%8B?type=S']
```

### 分析页面

这个应该都会了……

### setting的使用

#### 设置log级别

每次打印的时候都会出来一堆东西，不利于我们观察，我们想只看到我们自己打印的东西，可以在douban_book文件夹下的setting.py 文件中设置log级别。

在setting.py中添加一行：

> LOG_LEVEL ='WARNING'

#### 设置请求头

在使用`resquests`爬取网页的时候我们可以设置请求头，那么在scrapy中怎么设置请求头呢？

一种方法就是在setting.py中设置，在setting文件中找到

> #Crawl responsibly by identifying yourself (and your website) on the user-agent
>
> USER_AGENT = 'douban_book (+http://www.yourdomain.com)'

其中可以设置`USER_AGENT` 伪装成浏览器。

> USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.37'

#### 设置robots协议

在setting中还可以设置是否遵循`robots协议`(默认为Turn)，一般要更改为False。

设置`robots协议`

```python
# Obey robots.txt rules
ROBOTSTXT_OBEY = False   # 默认为Ture   
```

### parse函数的使用

当一个页面下载完成后，Scrapy引擎会回调一个我们指定的页面解析函数（默认为parse方法）解析页面。

```python
def parse(self, response):
    pass
```

其中response可以看成是下载到的页面，有两个方法可以解析页面:xpath,css

#### 获取一个页面的图书

```python
book_list = response.xpath('//ul[@class="subject-list"]/li')
for book in book_list:
    # 获取书名
    name = book.xpath('.//h2/a/@title').get()
    # 获取作者、出版社、出版日期、价格
    pub = book.xpath('.//div[@class="pub"]/text()').get().strip()
    # 评分
    rating_nums = book.xpath('.//span[@class="rating_nums"]/text()').get()
    print(f'name:{name}, pub:{pub}, rating_nums:{rating_nums}')
    
```

get() : 这个方法返回的是一个string字符串，是list数组里面的第一个字符串,没有就返回None

getall() : 这个方法返回的是一个数组list, 里面包含了多个string，如果只有一个string，则返回['ABC']这样的形式。

#### 翻页

```python
# -*- coding: utf-8 -*-
import scrapy


class DbSpider(scrapy.Spider):
    ...
    start = 0;    # 用于改变页码

    def parse(self, response):
      	... 
        self.start += 20
        if self.start < 100:
            next_url = f'https://book.douban.com/tag/%E7%BC%96%E7%A8%8B?type=S&start={self.start}'
            yield scrapy.Request(next_url, callback=self.parse)
        
```

设置start参数来改变页码，每爬取一个页面start加20，每页有20本书。

```python
yield scrapy.Request(next_url, callback=self.parse)
```

这里我们通过 `yield` 来发起一个请求，并通过 `callback` 参数为这个请求添加回调函数，在请求完成之后会将响应作为参数传递给回调函数。

#### db.py

```python
# -*- coding: utf-8 -*-
import scrapy


class DbSpider(scrapy.Spider):
    name = 'db'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/%E7%BC%96%E7%A8%8B?type=S']
    start = 0;

    def parse(self, response):
        book_list = response.xpath('//ul[@class="subject-list"]/li')
        print(len(book_list))
        for book in book_list:
            # 获取书名
            name = book.xpath('.//h2/a/@title').get()
            # 获取作者、出版社、出版日期、价格
            pub = book.xpath('.//div[@class="pub"]/text()').get().strip()
            # 评分
            rating_nums = book.xpath('.//span[@class="rating_nums"]/text()').get()
            print(f'name:{name}, pub:{pub}, rating_nums:{rating_nums}')
            
        self.start += 20
        if self.start < 100:
            # 翻页
            next_url = f'https://book.douban.com/tag/%E7%BC%96%E7%A8%8B?type=S&start={self.start}'
            yield scrapy.Request(next_url, callback=self.parse)
```

