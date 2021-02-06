## Spider

- Spider是用于为特定网站（或在某些情况下，一组网站）抓取和解析网页的自定义行为的位置。

### Spider工作流程

scrapy爬虫开启，调用`start_requests`方法，返回`Response`对象给回调函数（默认为`parse`），parse函数解析页面，返回`Request` 、` dicts` 或 `Item`对象，如果是`Request`对象则返回给设定的回调函数，` dicts` 或 `Item`对象交给`piplines`处理。当然中间还有其他步骤，这里只是主要的。

- start_requests源码

```python
    def start_requests(self):
        cls = self.__class__
        if method_is_overridden(cls, Spider, 'make_requests_from_url'):
            ...
            for url in self.start_urls:
                yield self.make_requests_from_url(url)
        else:
            for url in self.start_urls:
                yield Request(url, dont_filter=True)

    def make_requests_from_url(self, url):
        """ This method is deprecated. """
        return Request(url, dont_filter=True)
```

从中可以看出`start_requests`就是遍历了`start_urls`，返回start_urls里面的每个地址的`Request`对象

- - Request对象用来描述一个HTTP请求	

  - Response对象表示的HTTP响应

  - `start_urls`：当没有指定特定url时，scrapy开始爬取的url列表。

  - `parse`函数：这是返回`Response`对现时`未指定`回调函数，使用的`默认回调函数`。用于解析页面，提取数据

  ```
  def parse(self, response):
      pass
  ```

  - 参数：
    - response：对请求地址的响应，可以用来解析请求地址的页面
  - 返回：
    - **可迭代**的 `Request` 、` dicts` 或 `Item`对象

我们可以重写`start_requests`来处理一些问题，比如：

当需要在启动时以POST登录某个网站，可以`重写start_requests`函数。

```python
class MySpider(scrapy.Spider):
    name = 'myspider'
    def start_requests(self):
        # 设置回调函数为logged_in
        yield scrapy.FormRequest("http://www.example.com/login",
                                   formdata={'user': 'john', 'pass': 'secret'},
                                   callback=self.logged_in)
        
    def logged_in(self, response):
        pass
```

### 实现一个Spider

- 继承scrapy.Spider

  ```python
  class mySpider(scrapy.Spider)：
  ```

- 为Spider取名

  ```python
  name = 'myspider'
  ```

- 设定起始爬取点

  ```python
  start_urls = []
  ```

- 实现页面解析函数

  ```python
  	def parse(self, response):
  		pass
  ```
  
  ```python
  class mySpider(scrapy.Spider):
  	name = 'myspider'
	start_urls = []
  	
  	def parse(self, response):
  		pass
  ```
  
  





