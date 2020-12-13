## scrapy简介及安装

> Scrapy 是一套基于基于`Twisted`的异步处理框架，纯python实现的爬虫框架，用户只需要定制开发几个模块就可以轻松的实现一个爬虫，用来抓取网页内容以及各种图片，非常之方便～

安装scrapy

> pip install scrapy

验证安装是否成功

```python
import scrapy
scrapy.version_info   # (1, 6, 0)
```

导入scrapy,然后输出版本号,我的是1.6.0版本

## 第一个scrapy爬虫

#### 创建scrapy项目

> 1. scrapy startproject example   # 创建项目
> 2. cd example   # 进入项目
> 3. scrapy genspider example  example.com    # 创建爬虫文件

在命令行输入:

> scrapy startproject example

这个命令在当前文件夹下创建一个名为example的项目

目录结构：

> example
> ├── example
> │   ├── \_\_init\_\_.py
> │   ├── items.py
> │   ├── middlewares.py
> │   ├── pipelines.py
> │   ├── \_\_pycache\_\_
> │   ├── settings.py
> │   └── spiders
> │       ├── \_\_init\_\_.py
> │       └──\_\_pycache\_\_
> └── scrapy.cfg

这些文件我们先不管。

#### 创建爬虫文件

创建了项目后在命令行中有提示：

>You can start your first spider with:
>
>- cd example
>- scrapy genspider example example.com

cd example进入example文件夹

scrapy genspider example example.com 创建名为example，域名为example.com的爬虫文件

比如我们要爬取京东, 可以进入创建好的项目，在项目下创建名我jd， 域名为jd.com的爬虫文件即：

> - cd example
>
> - scrapy genspider jd jd.com

 这时候在spiders文件夹下会出现一个jd.py文件

文件内容如下

```python
# -*- coding: utf-8 -*-
import scrapy

class JdSpider(scrapy.Spider):
    name = 'jd'   # 爬虫名
    allowed_domains = ['jd.com']   # 允许在jd.com域名下爬取
    start_urls = ['http://jd.com/']   # 爬虫开始的位置
    
    def parse(self, response):
        pass
```

- `name`	是爬虫名用于启动爬虫
- `allowed_domains `  是允许爬取的域名
- `start_urls ` 定义爬虫爬取的起始点，起始点可以是多个，这里只有一个。
- `parse`  一般是解析页面的。

当然也可以自己创建一个爬虫文件。

#### 启动爬虫

在项目文件夹下，即上面cd example后进入的文件夹。在命令行中输入`scrapy  crawl <spider_name>`，启动刚创建好的爬虫：	

> scrapy crawl jd

这样我们就创建一个scrapy爬虫并启动了

