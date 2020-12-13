## scrapy下载中间件（Downloader Middleware）

### 介绍

> 下载器中间件是在引擎及下载器之间的特定钩子(specific hook)，处理Downloader传递给引擎的response。 其提供了一个简便的机制，通过插入自定义代码来扩展Scrapy功能。

### 下载中间件位置

在一个Spider中，spider发送一个Request对象给`engine（引擎）`，`engine（引擎）`最后把Request交给下载器。而在`engine（引擎）`和`下载器`中间还要经过一个`下载中间件`（Downloader Middleware）。

还有就是`下载器`把`response`对象交给``engine`的时候要经过下载器中间件。

### 下载中间件的实现

#### 定义类

- 在项目文件夹下找到`middlewares.py`文件，没有就创建一个

  ```python
  class ExampleDownloaderMiddleware(object):
      def process_request(self, request, spider):
          return None
      
      def process_response(self, request, response, spider):
          return response
  
  ```

  - 其中``process_request`是==引擎把`Request`对象交给下载器时==经过的下载中间件，当每个==request==通过下载中间件时，该方法被调用。
  - 而`process_response`是==下载器把`Response`对象交给引擎==时经过的下载中间件,当每个==response==通过下载中间件时，该方法被调用。

- 根据不同的用求编写process_request或process_response

##### process_request

参数：

- **request** (`Request`对象) – 处理的request
- **spider** (`Spider`对象) – 该request对应的spider

在`process_request`中可以定义请求头，代理等等

- 设置请求头：

  ```python
  def process_request(self, request, spider):
      request.headers['User-Agent'] = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Mobile Safari/537.36'
  ```

  - 这样我们就设定了请求头了，当然我们可以定义多个请求头，模拟不同的浏览器信息

- 设置代理

  ```python
  def process_request(self, request, spider):
      request.meta["proxy"]= 'http://127.0.0.0:8080'
  ```

  - 代理设置要在request.meta中。

  

##### process_response

- 参数：
  - **request** (`Request` 对象) – response所对应的request
  - **response** (`Response` 对象) – 被处理的response
  - **spider** (`Spider`对象) – response所对应的spider

在 `process_response` 中返回不同，就会执行不同的操作

- 返回
  -  **request** 会把request对象交给下载器，重新下载
  - **response** 把response对象交给引擎



### setting中开启

```python
DOWNLOADER_MIDDLEWARES = {
   'example.middlewares.ExampleDownloaderMiddleware': 543,
}
```

根据自己定义的类开启，可以定义多个

  

