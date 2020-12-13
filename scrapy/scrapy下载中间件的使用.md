### 项目分析

在爬取酷我音乐排行榜的每一首歌时，酷我音乐每个`rid`代表一首歌，我们可以通过请求酷我的`api`获取每页歌曲的`rid`。比如获取获取酷我热歌榜第一页的歌曲，api地址：

> http://www.kuwo.cn/api/www/bang/bang/musicList?bangId=16&pn=1&rn=30&httpsStatus=1&reqId=faa2a150-ab10-11ea-b58f-eba6b579f468

而请求这个`api`地址需要在请求头里添加`Cookie` 和 `csrf`，并且``Cookie` 里的kw_token的值要和`csrf`的值相等，比如这样：

```
headers = {
	'Cookie': 'kw_token=6A3S4588YMS',
	'csrf': '6A3S4588YMS'
}
```

下面我们就用下载中间件来设置headers。

### 创建爬虫

```shell
scrapy startproject kuwo_music
cd kuwo_music
scrapy genspider kw kuwo.cn
```

创建了一个name为kw的爬虫了

### 下载中间件的使用

- 修改`middlewares.py`文件为

```python
class KuwoMusicDownloaderMiddleware:
    
    def process_request(self, request, spider):
        request.headers['User-Agent'] = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Mobile Safari/537.36'
        request.headers['csrf'] = '6A3S4588YMS'
        request.cookies = {'kw_token':'6A3S4588YMS'}
        
        return None
```

在这里修改了请求头, 还有cookies。

_`注意`_：cookies不能在headers中设置。

- 在`setting.py`文件中开启`KuwoMusicDownloaderMiddleware`

  ```python
  DOWNLOADER_MIDDLEWARES = {
     'kuwo_music.middlewares.KuwoMusicDownloaderMiddleware': 543,
  }
  ```

### Spider的使用

- 修改`kw.py`文件

  ```python
  # -*- coding: utf-8 -*-
  import scrapy
  
  
  class KwSpider(scrapy.Spider):
      name = 'kw'
      allowed_domains = ['kuwo.cn']
      start_urls = ['http://www.kuwo.cn/api/www/bang/bang/musicList?bangId=16&pn=1&rn=30&httpsStatus=1&reqId=faa2a150-ab10-11ea-b58f-eba6b579f468']
  
      def parse(self, response):
          print(response.request.headers)
          print(response.text)
  ```

  打印`headers`看看是否设置成功，这里只是下载中间件的使用，就不继续了。

### 启动爬虫

```shell
scrapy crawl kw
```

