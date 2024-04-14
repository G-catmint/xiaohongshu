import requests
import execjs


class XiaoHongShu:
    def __init__(self):
        self.headers = {
            "authority": "edith.xiaohongshu.com",
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "origin": "https://www.xiaohongshu.com",
            "pragma": "no-cache",
            "referer": "https://www.xiaohongshu.com/",
            "^sec-ch-ua": "^\\^Chromium^^;v=^\\^122^^, ^\\^Not(A:Brand^^;v=^\\^24^^, ^\\^Google",
            "sec-ch-ua-mobile": "?0",
            "^sec-ch-ua-platform": "^\\^Windows^^^",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "x-b3-traceid": "c4b863585f68e58c",
        }
        self.url = "https://edith.xiaohongshu.com/api/sns/web/v2/comment/page"
        self.params = {
            "note_id": "660c4798000000001a00e82a",
            "cursor": "",
            "top_comment_id": "",
            "image_formats": "jpg,webp,avif"
        }
        self.cookies = {
            "abRequestId": "409145d4-b567-569e-afcb-775f0a5cda14",
            "xsecappid": "xhs-pc-web",
            "a1": "18ed18338cazbbfuwvyjnulkml45b0jtajgto9cip50000407842",
            "webId": "6cd7528d94f9edcb55164b4e4078178f",
            "gid": "yYdfyYqqSy04yYdfyYqqYVjSS0uDDi7EhvVIk3U71T6149282D8V9l88848WY4J8JJdi8fjW",
            "web_session": "030037a12ba2ec380123d4b060214a23965c43",
            "webBuild": "4.11.0",
            "websectiga": "3fff3a6f9f07284b62c0f2ebf91a3b10193175c06e4f71492b60e056edcdebb2",
            "sec_poison_id": "263f2405-35ca-4791-b7ef-dcef4a107fe9"
        }

    @staticmethod
    def open_js(file, func, data=None):
        js = execjs.compile(open(file, encoding='utf-8').read()).call(func, data)
        return js

    def req_info(self):
        js = self.open_js("./xhs全扣.js","main","/api/sns/web/v2/comment/page?note_id=65f4813b000000001203df8a&cursor=&top_comment_id=&image_formats=jpg,webp,avif")
        js['X-t'] = str(js['X-t'])
        header = {**self.headers, **js}
        print(header['X-t'])
        print(type(header['X-t']))
        response = requests.get(url=self.url,headers=header,cookies=self.cookies,params=self.params)
        print(response.text)
        print(response)


    def __del__(self):
        pass


if __name__ == '__main__':
    xhs = XiaoHongShu()
    xhs.req_info()

