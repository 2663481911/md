## scrapy-redis使用

### 环境

- 安装scrapy-redis库

  ```
  pip install scrapy-redis
  ```

- 安装redis

  ​	linux下

  ```shell
  sudo apt-get install redis-server
  ```

  - 启动redis

  ```shell
  /etc/init.d/redis-server start
  ```

### 项目需求

- 爬取酷我音乐排行榜的歌曲
  - 歌曲地址
  - 歌名

### 分析

……

### 创建项目

```shell
scrapy startproject kuwo_music
cd kuwo_music
scrapy genspider kw kuwo.cn
```

### spider使用，kw.py文件

```python
# -*- coding: utf-8 -*-
import scrapy
import json

class KwSpider(scrapy.Spider):
    name = 'kw'
    allowed_domains = ['kuwo.cn']

    def start_requests(self):
        """设置headers和cookies"""
        cookies = {'kw_token': '6A3S4588YMS'}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Mobile Safari/537.36',
            'csrf': '6A3S4588YMS'
        }
        start_url = 'http://www.kuwo.cn/api/www/bang/bang/musicList?bangId=16&rn=30&httpsStatus=1&reqId=faa2a150-ab10-11ea-b58f-eba6b579f468'
        for i in range(1, 11):
            url = f'{start_url}&pn={i}'
            yield scrapy.Request(url, headers=headers, cookies=cookies)

    def parse(self, response):
        """获取rid"""
        text_json = json.loads(response.text)
        music_list = text_json['data']['musicList']
        for music in music_list:
            music_rid = music['musicrid'].split('_')[1]
            music_name = music['name']

            rid_url = f'http://www.kuwo.cn/url?format=mp3&rid={music_rid}&response=url&type=convert_url3'
            yield scrapy.Request(rid_url, callback=self.get_musicUrl, meta={'music_name':music_name})
            break

    def get_musicUrl(self, response):
        """获取歌曲地址"""
        music_name = response.meta['music_name']
        music_url = json.loads(response.text)['url']
        yield {'music_name': music_name, 'music_url': music_url}

```

- `start_requests`：设置请求头和cookies，处理请求热歌榜api的前10页地址
- `parse`：获取api中的`rid`和`name`，用rid来合成歌曲地址所在页面的地址，并返回Request对象，设置回调函数为`get_musicUrl`
- `get_musicUrl`:获取歌曲地址

### scrapy-redis使用

在`setting.py`文件中添加

```python
# 确保request存储到redis中
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 确保所有爬虫共享相同的去重指纹
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 设置redis为item pipeline
ITEM_PIPELINES = {
	'scrapy_redis.pipelines.RedisPipeline': 300
}

# 在redis中保持scrapy-redis用到的队列，不会清理redis中的队列，从而可以实现暂停和恢复的功能。
SCHEDULER_PERSIST = True

# 设置连接redis信息
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
```

### 开启爬虫

```shell
scrapy crawl kw
```

这样就创建好了一个scrapy-redis爬虫。看看是不是每次都是从不同的位置开始爬虫呢。