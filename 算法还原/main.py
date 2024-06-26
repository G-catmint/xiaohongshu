"""
本代码只适用于https://edith.xiaohongshu.com/api/sns/web/v1/homefeed接口 
data参数什么的 请自行改进
仅供交流学习 请勿用作商业用途
"""

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
    # 请补充自己的cookie
    cookie = {
        "a1": "",
        "web_session": ""
    }
    xhs = Xhs()
    xhs.req_info(cookie)


