# -*- coding: utf-8 -*-
import scrapy


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['https://book.jd.com/']

    def parse(self, response):
        # print(response.text)
        pass


