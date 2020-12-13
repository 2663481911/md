'''
@encoding: utf-8
@Author: lss
@Date: 2020-06-02 10:30:18
@LastEditTime: 2020-06-05 22:41:29
@Description: file content
'''
# -*- coding: utf-8 -*-
import scrapy


class DbSpider(scrapy.Spider):
    name = 'db'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/%E7%BC%96%E7%A8%8B?type=S']
    start = 0

    def parse(self, response):
        book_list = response.xpath('//ul[@class="subject-list"]/li')
        for book in book_list:
            # 获取书名
            name = book.xpath('.//h2/a/@title').get()
            # 获取作者、出版社、出版日期、价格
            pub = book.xpath('.//div[@class="pub"]/text()').get().strip()
            # 评分
            rating_nums = book.xpath('.//span[@class="rating_nums"]/text()').get()
            yield {
                'name':name,
                'pub':pub,
                'rating_nums':rating_nums
            }
            
        self.start += 20
        if self.start < 100:
            next_url = f'https://book.douban.com/tag/%E7%BC%96%E7%A8%8B?type=S&start={self.start}'
            yield scrapy.Request(next_url, callback=self.parse)
