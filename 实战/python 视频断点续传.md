## python 视频断点续传

> 将下载或上传任务（一个文件或一个压缩包）人为的划分为几个部分，每一个部分采用一个线程进行上传或下载，如果碰到网络故障，可以从已经上传或下载的部分开始继续上传下载未完成的部分，而没有必要从头开始上传下载。用户可以节省时间，提高速度。

### 一、分割视频

#### 1、分割的每个小部分的大小：

```python
size = 1024 * 100    # 100k
```

#### 2、获取视频大小：

> 当在请求上设置stream=True时，没有立即请求内容，只是获取了请求头。推迟下载响应体直到访问 `Response.content` 属性

```python
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
}
resp = requests.get(url, headers=headers, stream=True)
content_length = resp.headers['content-length']
```

#### 3、分割视频：

设置请求头里面的`Range`参数

可以分割成多少个视频：

```python
count = int(content_length) // size
```

设置Range:

> `Range`：告知服务端，客户端下载该文件想要从指定的位置开始下载,格式：
>
> ​				'Range': 'bytes=start-end'。
>
> ​				start开始位置， end结束位置。

```python
range_liat = []
for i in range(count):
    start = i * size   # 开始位置
    # 结束位置
    if i == count - 1:
    	end = content_length   # 最后的一部分视频
    else:
    	end = start + size
    if i > 0:
    	start += 1
    headers_range = {'Range': f'bytes={start}-{end}'}
    range_list.append(headers_range)
```

![image-20200516092946185](https://raw.githubusercontent.com/2663481911/picGo_img/master/20200516092947.png)

### 二、请求视频

#### 1、设置请求头

```python
for i, headers_range in enumerate(range_list):
	headers_range.update(headers)
    resp = requests.get(url, headers=headers_range)
```

#### 2、保存视频

```python
with open(f'{i}', 'wb') as f:
    f.write(resp.content)
```

### 三、断点续传

确保下载文件的文件夹里没有其他文件

#### 1、获取保存视频的文件夹里面的文件的名称：

```python
import os
f_list = os.listdir(path)
```

#### 2、请求一小段视频时，先判断当前文件夹里是否存在，不存在才下载

```python
if not f'{i}' in ts_list:
    pass
```

### 四、合并视频

遍历小段视频保存的文件夹，按顺序保存到一个文件里就好了

```python
import os

def file_merge(path, path_name):
    """
    :param path: 小段视频保存文件夹路径
    :param path_name: 合并后保存位置+视频名字+格式
    """
    ts_list = os.listdir(path)
    with open(path_name, 'w') as f:
        pass
    with open(path_name, 'rb+') as fw:
        for i in range(len(ts_list)):
            # 小段视频路径
            path_name_i = os.path.join(path, f'{i}')
            with open(path_name_i, 'rb') as fr:
                buff = fr.read()
                fw.write(buff)
            # 删除文件
            os.remove(path_name_i)
    print('合并完成：', path)
```



### 五、完整代码：

#### 1、requests版本，多进程，没有进度条

```python
import os
import requests
from multiprocessing.pool import Pool

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
}
# 分割的每个视频大小100k
size = 1024 * 100


def get_range(url):
    """获取分割视频的位置"""
    resp = requests.get(url, headers=headers, stream=True)
    content_length = resp.headers['content-length']
    count = int(content_length) // size
    
    headers_list = []
    for i in range(count):
        start = i * size

        if i == count - 1:
            end = content_length
        else:
            end = start + size
        if i > 0:
            start += 1

        rang = {'Range': f'bytes={start}-{end}'}
        rang.update(headers)
        headers_list.append(rang)

    return headers_list


def down_file(url, headers, i, path):
    """
    :param url: 视频地址
    :param headers: 请求头
    :param i: 小段视频保存名称
    :param path: 保存位置
    """
    content = requests.get(url, headers=headers).content
    with open(f'{path}{i}', 'wb') as f:
        f.write(content)


if __name__ == '__main__':
    path = 'G:/s/'
    pool = Pool(8)   # 进程池
    url = ''
    
    for i, headers in enumerate(get_range(url)):
        ts_list = os.listdir(path)
        if not f'{i}' in ts_list:
            pool.apply_async(down_file, args=(url, headers, i, path))
            
    pool.close()
    pool.join()

```

#### 2、asyncio版本，异步，有进度条

```python
import asyncio
import os
from tqdm import tqdm
from aiohttp import ClientSession

headers = {
    'referer': 'https://www.bilibili.com/video',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0'
}
size = 1024 * 100  # 分割的每个视频长度


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


async def async_main(video_url, section_path):
    """
    分割视频，即设置请求头
    :param video_url: 视频地址
    :param section_path: 保存位置
    """
    async with ClientSession() as session:
        async with session.get(video_url, headers=headers) as resp:
            content_length = resp.headers['content-length']  # 获取视频长度
            range_list = get_range(content_length)

            sem = asyncio.Semaphore(50)   # 限制并发数量
            if not os.path.exists(section_path):
                os.mkdir(section_path)

            # 进度条
            with tqdm(total=int(content_length), unit='', ascii=True, unit_scale=True) as bar:
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


def main(video_url, section_path):
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(async_main(video_url, section_path))
    loop.run_until_complete(task)


if __name__ == '__main__':
    url = ''
    path = 'G:/s/'
    main(url, path)

    # 合并
    from f import file_merge
    file_merge(path, 'G:/1.mp4')

```

