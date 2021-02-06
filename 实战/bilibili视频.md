bilibili.py文件，获取视频地址和name

```python
def get_cidName(bv):
    """
    获取视频cid和name
    :param bv:视频 bv号
    :return cid, name 列表
    """
    pageList_url = f'https://api.bilibili.com/x/player/pagelist?bvid={bv}&jsonp=jsonp'
    resp = requests.get(pageList_url, headers=headers)
    
    if resp.status_code == 200:
        resp_json = resp.json()
        data_list = resp_json['data']
        
        cidName_list = []
        for data in data_list:
            cid = data['cid']
            name = data['part']
            cidName_list.append([cid, name])
            
        return cidName_list
    
    
def get_videoUrl(bv, cid):
    """
    获取视频地址：
    :param bv:  bv号
    :param cid: 各个视频的cid
    :return: 视频地址
    """
    play_url = f'https://api.bilibili.com/x/player/playurl?bvid={bv}&cid={cid}&otype=json'
    resp = requests.get(play_url, headers=headers)
    
    if resp.status_code == 200:
        resp_json = resp.json()
        video_url = resp_json['data']['durl'][0]['url']
        return video_url

    
def main(bv):
    cidName_list = get_cidName(bv)
    for cid, name in cidName_list:
        video_url = get_videoUrl(bv, cid)
        yield video_url, name
```

视频下载：

```python
import asyncio
import os
from tqdm import tqdm
from aiohttp import ClientSession

headers = {
    'referer': 'https://www.bilibili.com/video',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
}
size = 1024 * 100  # 分割的每个视频长度：100k
sem_num = 16   # 并发数量


def get_range(content_length):
    """
    :param content_length: 视频长度
    :return: 请求头：Range
    """
    count = int(content_length) // size  # 分割成几个视频
    range_list = []
    
    for i in range(count):
        start = i * size

        if i == count - 1:
            end = content_length
        else:
            end = start + size
        if i > 0:
            start += 1
            
        rang = {'Range': f'bytes={start}-{end}'}
        range_list.append(rang)
        
    return range_list


async def async_main(video_url, section_path, name):
    """
    分割视频，即设置请求头
    :param video_url: 视频地址
    :param section_path: 保存位置
    """
    async with ClientSession() as session:
        async with session.get(video_url, headers=headers) as resp:
            content_length = resp.headers['content-length']  # 获取视频长度
            range_list = get_range(content_length)

            sem = asyncio.Semaphore(sem_num)   # 限制并发数量
            if not os.path.exists(section_path):
                os.mkdir(section_path)

            # 进度条
            with tqdm(total=int(content_length), desc=name,  unit='', ascii=True, unit_scale=True) as bar:
                down_list = os.listdir(section_path)
                tasks = []
                for i, headers_range in enumerate(range_list):
                    # 判断是否已经下载
                    if f'{i}' not in down_list:
                        headers_range.update(headers)
                        task = down_f(session, video_url, headers_range, i, section_path, sem, bar)
                        tasks.append(task)
                    else:
                        bar.update(size)
                await asyncio.gather(*tasks)


async def down_f(session, video_url, headers_range, i, section_path, sem, bar):
    """下载"""
    async with sem:   # 限制并发数量
        async with session.get(video_url, headers=headers_range) as resp:
            chunks = b''
            async for chunk in resp.content.iter_chunked(1024):
                chunks += chunk

            with open(f'{section_path}{i}', 'wb') as f:
                f.write(chunks)
                bar.update(size)  # 更新进度条

                
def file_merge(path, path_name):
    """
    视频合并
    :param path: 小段视频保存文件夹路径
    :param path_name: 合并后保存位置+视频名字+格式
    """
    ts_list = os.listdir(path)
    with open(path_name, 'w') as f:
        pass
    with open(path_name, 'rb+') as fw:
        for i in range(len(ts_list)):
            path_name_i = os.path.join(path, f'{i}')
            with open(path_name_i, 'rb') as fr:
                buff = fr.read()
                fw.write(buff)
            os.remove(path_name_i)   # 删除文件
            
            
def main(video_url, section_path, name):
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(async_main(video_url, section_path, name))
    loop.run_until_complete(task)

if __name__ == '__main__':
    import bilibili
    
    bv = 'BV1xs411Q799'
    for video_url, name in bilibili.main(bv):
        path = 'G:/s/'   # 临时保存位置
        main(video_url, path, name)
        file_merge(path, f'G:/{name}.mp4')
```

![image-20200517101619478](bilibili%E8%A7%86%E9%A2%91.assets/image-20200517101619478.png)