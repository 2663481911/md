import requests
from pprint import pprint


def get_videoUrl(bv, cid):
    url = f'https://api.bilibili.com/x/player/playurl?bvid=BV1xs411Q799&cid={cid}&otype=json'
    resp_json = requests.get(url).json()
    # pprint(resp_json)
    durl_list = resp_json['data']['durl']
    url = durl_list[0]['url']
    return url


def get_cidName_list(bv):
    url = f'https://api.bilibili.com/x/player/pagelist?bvid={bv}&jsonp=jsonp'
    resp_json = requests.get(url).json()
    # pprint(resp_json)
    cidName_list = []
    data_lsit = resp_json['data']
    for data in data_lsit:
        cid = data['cid']
        name = data['part']
        cidName_list.append([cid, name])
    # pprint(cidName_list)
    return cidName_list


def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.72',
        'referer': 'https://www.bilibili.com/video/'
    }

    bv = 'BV1xs411Q799'
    cidName_list = get_cidName_list(bv)
    for cid, name in cidName_list:
        video_url = get_videoUrl(bv, cid)
        headers = requests.get(video_url, headers=headers, stream=True).headers

        print(video_url, '\n', headers)
        break


if __name__ == '__main__':
    main()
