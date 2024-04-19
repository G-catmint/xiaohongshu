import time
import requests
import execjs
import json


class Xhs:
    def __init__(self):
        self.data = {"cursor_score":"","num":18,"refresh_type":1,"note_index":0,"unread_begin_note_id":"","unread_end_note_id":"","unread_note_count":0,"category":"homefeed_recommend","search_key":"","need_num":8,"image_formats":["jpg","webp","avif"],"need_filter_image":False}
        self.datas =json.dumps(self.data,separators=(',', ":"))
        self.url = 'https://edith.xiaohongshu.com/api/sns/web/v1/homefeed'
        self.headers = {
            'Accept':'application/json,text/plain, */*',
            'Accept-Encoding':'gzip,deflate,br,zstd',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Cache-Control':'no-cache',
            'Content-Length':'278',
            'Content-Type':'application/json;charset=UTF-8',
            'Origin':'https://www.xiaohongshu.com',
            'Pragma':'no-cache',
            'Referer':'https://www.xiaohongshu.com/',
            'Sec-Ch-Ua':'"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
            'Sec-Ch-Ua-Mobile':'?0',
            'Sec-Ch-Ua-Platform':'"Windows"',
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode':'cors',
            'Sec-Fetch-Site':'same-site',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'X-B3-Traceid':"fdb9ab3d6df48c8c",
            'X-S':"",
            'X-T':''
        }


    @staticmethod
    def open_js(file, func, *args):
        js = execjs.compile(open(file, encoding='utf-8').read()).call(func, *args)
        return js

    def req_info(self,cookie):
        data = self.open_js('./js_code.js', 'get_x_s', '/api/sns/web/v1/homefeed', self.data,cookie['a1'])
        self.headers['X-S'] = data[0]
        self.headers['X-T'] = str(data[1])
        response = requests.post(url=self.url,headers=self.headers,cookies=cookie,data=self.datas)
        print(response.text)
        print(response)


if __name__ == '__main__':
    cookie = {
        "abRequestId": "183b201e-5372-5614-81d3-9944be6b681d",
        "webBuild": "4.13.1",
        "xsecappid": "xhs-pc-web",
        "a1": "18ef3993899ddm7laqnf4pz4i65848het08ta1dv850000148635",
        "webId": "ff424613890e029bd733d62e087bd9b1",
        "gid": "yYdiqjj4qK98yYdiqjjqY8yfjjff6W10AIi4YhYUu43K2928Y4Yxd0888y4YKq28YdiDyKKj",
        "web_session": "030037a112e4003994e738f659214a5115c33e"
    }
    xhs = Xhs()
    xhs.req_info(cookie)


