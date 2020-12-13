# -*- coding: utf-8 -*-
import scrapy
import json
import re
from pprint import pprint


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=12398725&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&rid=0&fold=1']
    page = 0   # 标记评论页码

    def parse(self, response):
        # 转成字典格式
        re_t = re.findall(r'fetchJSON_comment98\((.*)\);', response.text)[0]
        json_t = json.loads(re_t)
        
        coment_list = json_t['comments']
        for comment in coment_list:
            id = comment['id']   
            content = comment['content']   # 评论
            referenceName = comment['referenceName']
            creationTime = comment['creationTime']
            yield {'_id':id, 'content':content, 'referenceName':referenceName, 'creationTime':creationTime}
        
        self.page += 1
        if self.page < 20:
        
            next_url = f'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=12398725&score=0&sortType=5&page={self.page}&pageSize=10&isShadowSku=0&rid=0&fold=1'
            yield scrapy.Request(next_url)
