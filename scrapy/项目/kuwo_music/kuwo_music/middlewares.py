


class KuwoMusicDownloaderMiddleware:
    
    def process_request(self, request, spider):
        request.headers['User-Agent'] = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Mobile Safari/537.36',
        request.cookies = {'kw_token':'6A3S4588YMS'}
        request.headers['csrf'] = '6A3S4588YMS'
        
        return None
    