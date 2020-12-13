import requests
from pprint import pprint

headers = {
    'Cookie': 'kw_token=6A3S4588YMS',
    'csrf': '6A3S4588YMS'
}


def get_music_rid_name(url):
    '''获取rid和name'''
    text_json = requests.get(url, headers=headers).json()
    pprint(text_json)
    musicList = text_json['data']['musicList']

    music_list = []
    dit = {}

    for music in musicList:
        dit['rid'] = music['musicrid'].split('_')[1]
        dit['name'] = music['name']
        music_list.append(dit.copy())

    return music_list


def get_music_url(rid_url):
    '''获取歌曲地址'''
    resp_json = requests.get(rid_url).json()
    music_url = resp_json['url']
    return music_url


def main():
    url = 'http://www.kuwo.cn/api/www/bang/bang/musicList?bangId=93&pn=1&rn=30'
    music_list = get_music_rid_name(url)
    for music in music_list:
        rid = music['rid']
        rid_url = f'http://www.kuwo.cn/url?format=mp3&rid={rid}&response=url&type=convert_url3'
        music_url = get_music_url(rid_url)
        print(music_url, music['name'])


if __name__ == '__main__':
    main()
