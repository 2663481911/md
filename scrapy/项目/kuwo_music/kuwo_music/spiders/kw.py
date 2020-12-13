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
        start_url = 'http://www.kuwo.cn/api/www/bang/bang/musicList?bangId=16&rn=30&httpsStatus=1&reqId=faa2a150-ab10' \
                    '-11ea-b58f-eba6b579f468 '
        for i in range(1, 5):
            url = f'{start_url}&pn={i}'
            yield scrapy.Request(url, headers=headers, cookies=cookies)

    def parse(self, response):
        """获取rid"""
        text_json = json.loads(response.text)
        if text_json:
            music_list = text_json['data']['musicList']
            for music in music_list:
                music_rid = music['musicrid'].split('_')[1]
                music_name = music['name']

                rid_url = f'http://www.kuwo.cn/url?format=mp3&rid={music_rid}&response=url&type=convert_url3'
                yield scrapy.Request(rid_url, callback=self.get_musicUrl, meta={'music_name':music_name})
                # break

    def get_musicUrl(self, response):
        """获取歌曲地址"""
        music_name = response.meta['music_name']
        music_url = json.loads(response.text)['url']
        # print({'music_name': music_name, 'music_url': music_url})

        yield {'music_name': music_name, 'music_url': music_url}
        # 下载
        yield scrapy.Request(music_url, callback=self.down_music, meta={'music_name': music_name})

    def down_music(self, response):
        music_name = response.meta['music_name']
        with open(f'/media/lss/Linux Windows/音乐/{music_name}.mp4', 'wb') as f:
            f.write(response.body)
            print('下载', music_name)
