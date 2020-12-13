### 数据格式

我们可以把爬取到的数据封装成`字典或item对象`交给`pipelines`处理。

- 字典：python提供的一种数据结构。
- item: 是保存爬取到的数据的容器；其使用方法和`python字典`类似， 并且提供了额外保护机制来`避免拼写错误`导致的未定义字段错误。

### 定义item

- 可以通过创建一个 `scrapy.Item` 类， 并且定义类型为 `scrapy.Field` 的类属性来定义一个Item。

在项目文件夹下的items.py文件中定义item

```python
import scarpy
class DoubanBookItem(scrapy.Item):
    name = scrapy.Field()
    pub = scrapy.Field()
    rating_nums = scrapy.Field()
```

- `Field`：是内置的字典类的一个别名，并没有提供额外的方法或者属性。换句话说， `Field` 对象完完全全就是Python字典(dict)。

还有以爬取豆瓣图书图书为例。

在这里定义三个属性，就和字典的键差不多。

- name : 用于保存书名
- pub ：用于保存出版社、作者等等信息
- rating_nums : 用于保存书籍评分

### item使用

在spider下面的爬虫文件中

```python
import scrapy
from douban_book.items import DoubanBookItem

class DbSpider(scrapy.Spider):
    ...
    def parse(self, response):
        book_list = response.xpath('//ul[@class="subject-list"]/li')
        for book in book_list:
            item = DoubanBookItem()
            item['name'] = book.xpath('.//h2/a/@title').get()
            item['pub'] = book.xpath('.//div[@class="pub"]/text()').get().strip()
            item['rating_nums'] = book.xpath('.//span[@class="rating_nums"]/text()').get()
            yield item
            
        ...
```

- 首先我们导入item对象

```python
from douban_book.items import DoubanBookItem
```

- 然后创建一个item对象

```python
item = DoubanBookItem()
```

- item对象是自定义的python字典，我们可以和使用字典一样使用它

```python
item['name'] = book.xpath('.//h2/a/@title').get()
item['pub'] = book.xpath('.//div[@class="pub"]/text()').get().strip()
item['rating_nums'] = book.xpath('.//span[@class="rating_nums"]/text()').get()
```

`注意`:

- item的键只有我们定义了才可以使用，不然会报错。

- 存入数据库记得把item对象转成字典。

最后我们以`item`的形式返回了爬取到的数据。

