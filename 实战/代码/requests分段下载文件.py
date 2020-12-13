import requests

url = 'https://www.baidu.com/'
with requests.get(url, stream=True) as r:
    print(r.headers)
# iter_lines
# for line in r.iter_lines():
#     if line:
#         decoded_line = line.decode('utf-8')
#         print('line:', decoded_line)

    # iter_content
    # for chunk in r.iter_content(chunk_size=20):
    #     if chunk:
    #         decoded_chunk = chunk.decode('utf-8')
    #         print(decoed_chunk)
