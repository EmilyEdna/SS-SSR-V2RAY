import requests
import re


class V2RAY:
    def __init__(self):
        self = self

    def GetHtmlText(self):
        vmess=[]
        SSURL = "https://xxx.ishadowx.org/"
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

    def SaveFile(self, vmess):
        with open('V2RAY/V2RAY.txt', 'r+', encoding='utf-8') as f:
            f.seek(0)
            f.truncate()
        with open('V2RAY/V2RAY.txt', 'a', encoding='utf-8') as f:
            for data in vmess:
                f.write(data)
                f.write('\n')
