import requests
import json
import re
from pprint import pprint


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.72',
}
def get_comment(url):
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        text = resp.text
        pattern = re.compile(r'fetchJSON_comment98\((.*?)\);', re.S)
        t_data = pattern.search(text).group(1)
        t_json = json.loads(t_data)
        pprint(t_json)
        for comment in t_json['comments']:
            print(comment['content'])




if __name__ == '__main__':
    url = 'https://club.jd.com/comment/productPageComments.action?callback='\
        'fetchJSON_comment98&productId=11943853&score=0&sortType=5&page=0&pageSize=10'\
        '&isShadowSku=0&rid=0&fold=1'
    get_comment(url)
