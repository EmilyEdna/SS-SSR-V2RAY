import requests
import re
import base64
import pyzbar.pyzbar as pyzbar
from PIL import Image


class SS:
    def __init__(self):
        self = self

    def GetHtmlText(self):
        ImgPath = []
        SSURL = "https://ss.freess.info/#portfolio-preview"
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
        result = requests.get(SSURL, headers=headers).text
        res = re.findall(r'\"data:(.*?)\"', result)
        count = 0
        for item in res:
            count = count + 1
            if (count != 4) and (count != 6):
                data = item.split(',')[1]
                img = base64.urlsafe_b64decode(data + '=' *
                                               (4 - len(data) % 4))
                ImgPath.append('./' + str(count) + '.png')
                fw = open('./' + str(count) + '.png', 'wb')
                fw.write(img)
                fw.close()
        return ImgPath

    def QrCode(self, ImgPath):
        codebytes = []
        for item in ImgPath:
            pic = Image.open(item)
            codeinfos = pyzbar.decode(pic)
            for codeinfo in codeinfos:
                datainfo = codeinfo.data.decode('utf-8')
                codebytes.append(datainfo)
        return codebytes

    def SaveFile(self, bytes):
        with open('README.md', 'r+', encoding='utf-8') as f:
            f.seek(0)
            f.truncate()
        with open('README.md', 'a', encoding='utf-8') as f:
            for data in bytes:
                f.write(data)
                f.write('\n')
            f.write("以上SS链接每晚12点更新端口")