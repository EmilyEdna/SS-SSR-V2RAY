import requests
import re
import base64

class V2RAY(object):
    def __init__(self):
        self = self

    def GetHtmlText(self):
        vmess = []
        SSURL = "https://free.ishadowx.biz/"
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
        result = requests.get(SSURL, headers=headers).text
        res = re.findall(r'\"vmess:\W+[a-zA-Z0-9]+\W+\"', result)
        for item in res:
            item = re.findall(r'vmess:\W+[a-zA-Z0-9]+\W', item)
            vmess.append(item[0])
        return vmess

    def SaveFileSub(self, vmess):
        with open('V2RAY/V2RAYSub.txt', 'r+', encoding='utf-8') as f:
            f.seek(0)
            f.truncate()
        with open('V2RAY/V2RAYSub.txt', 'a', encoding='utf-8') as f:
            for data in vmess:
                result = (base64.b64encode((data + '\r\n').encode())).decode()
                f.write(result)

    def SaveFileLink(self, vmess):
        with open('V2RAY/V2RAYLink.txt', 'r+', encoding='utf-8') as f:
            f.seek(0)
            f.truncate()
        with open('V2RAY/V2RAYLink.txt', 'a', encoding='utf-8') as f:
            for data in vmess:
                f.write(data)
                f.write('\n')