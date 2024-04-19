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



    def req_info(self,cookie):
        data = json.dumps(cookie, separators=('; ',"=")).replace("\"","").replace("{","").replace("}","")
        with open("./jsweb.js","r",encoding="utf-8") as file:
            result = file.read().replace("'documentcookie'",data)
        headerxs = execjs.compile(result).call("main", '/api/sns/web/v1/homefeed', self.data)
        self.headers['X-S'] = headerxs['X-s']
        self.headers['X-T'] = str(headerxs['X-t'])
        response = requests.post(url=self.url,headers=self.headers,cookies=cookie,data=self.datas)
        print(response.text)
        print(response)


if __name__ == '__main__':
    # 请补充自己的cookie
    cookie = {
        "abRequestId": "6d996cd6-ccec-5200-b7de-52ccd892b90f",
        "webBuild": "4.13.1",
        "xsecappid": "xhs-pc-web",
        "a1": "18ef441eb51kudwugf5gf5b0eaw9g90bioqijc7p750000287221",
        "webId": "84598e75435d73e629d80fe8757c26e3",
        "gid": "yYdi44yiKy3DyYdi44ydDlSW2yT7fE7ki2kiAUW2D8d0E328jkj8DV888JYWJJy8KD0W0q0q",
        "web_session": "030037a1128fd23903ebea9d59214ade1b1b30"
    }
    xhs = Xhs()
    xhs.req_info(cookie)


