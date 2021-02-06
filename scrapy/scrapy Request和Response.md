### 请求与响应

Scrapy 使用 `Request`和 `Response` 对象来抓取网站。

- 通常, `Request`对象在`Spider`中生成并传递到`engine（引擎）`，engine交给`Scheduler（调度器）`再返回给`engine`然后到`Downloader（下载器）`，Downloader下载从`engine`发过来的Request请求，并返回一个 `Response`对象给`引擎`，引擎将该`Response`对象返回给发出请求的`Spider`。

- 工作原理

  <img src="scrapy Request和response.assets/scrapy原理.jpg" alt="scrapy工作原理" style="zoom: 50%;" />

  `spider(Request)` ——> `engine(Request)` ——> `Scheduler(在排队)(Request)` ——> `engine(Request)` ——>

  `Downloader(Response) `——> ` engine(Response)`  ——> `Spider`

- 就是获取一个网页的`Response对象`给回调函数

### Request对象

Request对象用来描述一个HTTP请求，下面是其构造器方法的参数列表：

```python
Scrapy.Request(url[, callback, method='GET', headers, body, cookies, meta, encoding='utf-8', priority=0, dont_filter=False, errback, flags])
```

- url : 请求地址
- callback ：回调函数，默认`spider的parse`函数
- method ：请求方法，默认为`GET`
- headers ：请求头。
- body : HTTP请求的正文，bytes或str类型。
- cookies : 请求cookie，可以是`dict` 或 `带有dict的list`。
- meta : `dict`，给响应处理函数传递信息，可以使用`response.meta`获得。在某些情况下，您可能要将参数传递给那些回调函数，以便稍后在第二个回调中接收参数。您可以使用该 属性.
- priority ：请求的优先级默认值为0，优先级高的请求优先下载。
- dont_filter=False ：是否过滤地址，就是不重复请求，默认是过滤。
- errback ：发生错误的时候处理的函数

### Response对象

- 表示HTTP响应，类型有
  - textResponse
  - HtmlResponse
  - XmlResponse

- 当一个页面下载完成时，下载器依据HTTP响应头部中的Content-Type信息创建某个Response的子类对象。通常爬取的网页，其内容是HTML文本，创建的便是HtmlResponse对象。

- HtmlResponse属性和方法

  - url：包含响应URL的字符串。

  - status：表示响应的HTTP状态码

  - headers：HTTP响应的头头部，类字典类型。可以使用 `get()` 以返回具有指定名称的第一个标头值来访问值，或者 `getlist()` 返回具有指定名称的所有标头值。例如，此调用将为您提供headers中的所有Cookie:

    ```python
    response.headers.getlist('Set-Cookie')
    ```

  - body：HTTP响应正文，bytes类型。

  - text：文本形式的HTTP响应正文，str类型

  - meta：即response.request.meta，在构造Request对象时，可将要传递给响应处理函数的信息通过meta参数传入；响应处理函数处理响应时，通过response.meta将信息取出。

  - urljoin(*url*)：通过将Response.url与可能的相对URL 组合来构造绝对URL。 `urlparse.urljoin`

  - selector：Selector对象用于在Response中提取数据。

  - xpath(query)：xpath选择器

  - css(query)：css选择器