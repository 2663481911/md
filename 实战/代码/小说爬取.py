import requests
from lxml import etree
from queue import Queue
from threading import Thread


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.72',
}


def get_pageUrlName(url):
    '''获取各章节地址和章节名'''
    resp = requests.get(url, headers=headers)
    html = etree.HTML(resp.text)
    dd_list = html.xpath('//div[@id="list"]/dl/dt[2]/following-sibling::dd')
    # 获取小说名
    title = html.xpath('//h1/text()')[0]
    pageUrlName_list = []
    dit = {}
    for dd in dd_list:

        dit['pageUrl'] = url + dd.xpath('./a/@href')[0]
        dit['pageName'] = dd.xpath('./a/text()')[0]
        pageUrlName_list.append(dit.copy())

    # print(pageUrlName_list)
    return pageUrlName_list, title


def get_content(page_url):
    '''获取内容'''
    resp = requests.get(page_url, headers=headers)
    html = etree.HTML(resp.text)
    content_list = html.xpath('//div[@id="content"]/text()')
    # print('\r\n'.join(content_list[:-1]))
    return '\r\n'.join(content_list[:-1])


def down_txt(q, fw):
    '''保存小说'''
    global index
    while not q.empty():
        i, page_url_name = q.get()
        # print(page_url_name, i)
        page_url = page_url_name['pageUrl']
        page_name = page_url_name['pageName']
        content = page_name + get_content(page_url)
        print('爬取-->', page_name)

        # 判断当前章节是否和标记的章节数一样
        while i > index:
            pass

        if index == i:
            print('保存', page_name)
            fw.write(content)
            index += 1


if __name__ == '__main__':
    url = 'https://www.lingdiankanshu.co/467479/'
    pageUrl_list, title = get_pageUrlName(url)
    # print(pageUrl_list)

    q = Queue()
    for i, page_url_name in enumerate(pageUrl_list):
        q.put([i, page_url_name])

    index = 0   # 记录保存章节数
    with open(f'{title}.txt', 'w', encoding='utf8') as fw:

        ts = []
        for i in range(10):
            t = Thread(target=down_txt, args=[q, fw])
            t.start()
            ts.append(t)

        for t in ts:
            t.join()
