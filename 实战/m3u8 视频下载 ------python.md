## m3u8 视频下载 ------python

### 文件格式

> m3u8 文件作为媒体播放列表时，其内部信息记录的是一系列媒体片段资源，顺序播放该片段资源，即可完整展示多媒体资源。

```
#EXTM3U   // 这个是M3U8文件必须包含的标签，并且必须在文件的第一行，所有的M3U8文件中必须包含这个标签。
#EXT-X-VERSION:3   // 版本号
#EXT-X-TARGETDURATION:8   // 该标签指定了媒体文件持续时间的最大值
#EXT-X-MEDIA-SEQUENCE:0   
#EXTINF:4.166667,   // 表示其后 URL 指定的媒体片段时长（单位为秒）
649132334cd000000.ts   // 媒体片段 URL
#EXTINF:5.500000,
649132334cd000001.ts
```

有的还有EXT-X-KEY标签：媒体片段可以进行加密，而该标签可以指定解密方法。

```
#EXT-X-KEY:METHOD=AES-128,URI="key.key"
```

### 请求m3u8文件，保存

##### 1、请求这个m3u8文件

https://youku.cdn7-okzy.com/20200320/17981_b5d8baf6/1000k/hls/index.m3u8

```python
url = 'https://youku.cdn7-okzy.com/20200320/17981_b5d8baf6/1000k/hls/index.m3u8'
text = requests.get(url, headers=headers).text
```

> ```
> #EXTM3U
> #EXT-X-VERSION:3
> #EXT-X-TARGETDURATION:8
> #EXT-X-MEDIA-SEQUENCE:0
> #EXTINF:4.166667,
> 649132334cd000000.ts
> #EXTINF:5.500000,
> 649132334cd000001.ts
> ···
> ```

请求得到一个.m3u8的文件，看看是否有EXT-X-KEY 标签，有就需要解密

##### 2、用正则来判断是否需要解密，即`EXT-X-KEY`是否存在

- 只要判断URI是否存在即可

```python
from Crypto.Cipher import AES   # 解密

pattern_key = re.compile('URI="(.*?)"')
key = pattern_key.findall(text)
# 判断是否需要解密
aes = ''
if key:
	key_url = parse.urljoin(url, key[0])
    # 取得key 16位密钥
	key_text = text = requests.get(key_url).text
    # 初始化AES
    aes = AES.new(key_text,AES.MODE_CBC,key_text)
```

##### 3、ts下载、保存

ts地址提取出来得到的是

```
649132334cd000000.ts  
```

需要合并成完整地址，地址合并可以用urllib.parse.urljoin

```python
from urllib import parse
# ts地址提取
pattern_ts = re.compile('.*?\.ts')
ts_list = pattern_ts.findall(text)

ts_url_list = []
for ts in ts_list:
    # 合并
	ts_url = parse.urljoin(url, ts)
    ts_url_list.append(ts_url)
```

请求ts文件, 得到ts媒体文件

在保存ts文件的时候顺序不能乱，不然合并的后得到的视频顺序不对，这个时候我们可以用enumerate

还要判断是否需要解密再保存

```python
for i, ts_url in enumerate(ts_url_list):
    con = requests.get(ts_url).content
    # 判断是否需要解密
    if aes:
        # 解密
        con = aes.decrypt(con)
    with open(f'{i}.ts', 'wb') as fw:
        fw.write(con)
```

##### 4、合并

获取文件夹下面的ts文件名

```python
# path ts文件保存位置
ts_list = os.listdir(path)   # 获取path下载的文件名
```

遍历ts文件合并为一个文件

```python
with open('path_name', 'ab') as fw:
    for i in range(len(ts_list)):
        with open(f'{i}.ts', 'rb') as fr:
        	fe.write(fr.read())
            
```

```python

import requests
import re
from Crypto.Cipher import AES   # 解密

def get_text(url):
    return requests.get(url, headers=headers).text


def get_aes(url, text):
	'''获取aes，用于解密'''
    pattern_key = re.compile('URI="(.*?)"')
    key = pattern_key.findall(text)
    if key:    
        key_url = parse.urljoin(url, key[0])    
        # 取得key 16位密钥    
        key_text = text = requests.get(key_url).text    
        # 初始化AES    
        aes = AES.new(key_text,AES.MODE_CBC,key_text)
        return aes


def get_ts_list(url, text):
    '''获取ts地址'''
    pattern_ts = re.compile('.*?\.ts')
    ts_list = pattern_ts.findall(text)
    ts_url_list = []
    for ts in ts_list:
        # 合并
        ts_url = parse.urljoin(url, ts)
        ts_url_list.append(ts_url)
    return ts_url_list


def down_ts(aes, i, ts_url, path):
    '''下载ts媒体文件'''
    con = requests.get(ts_url).content
    if aes:
        # 解密
        con = aes.decrypt(con)
    with open(f'{path}{i}.ts', 'wb') as fw:
        fw.write(con)

def merge_ts(path, save_path):
    '''合并ts'''
    ts_list = os.listdir(path) 
    with open(f'{save_path}', 'ab') as fw:
        for i in range(len(ts_list)):
            with open(f'{i}.ts', 'rb') as fr:
                fe.write(fr.read())

if __name__ == '__main__':
    url = 'https://youku.cdn7-okzy.com/20200320/17981_b5d8baf6/1000k/hls/index.m3u8'
    text = get_text(url)
    aes = get_aes(url, text)
    ts_list = get_ts_list(url, text)
    path = './m3u8/'   # 懒得判断了，自己创建
    for i, ts_url in enumerate(ts_list):
        down_ts(aes, i, ts_url, path)
    save_path = './1.mp4'
    merge_ts(path, save_path)
```

ps:不知道有没有打错····