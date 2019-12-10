import requests
import re
import base64


class SSR(object):
    def __init__(self):
        self = self

    def GetHtmlText(self):
        SSRArr = []
        SSURL = "https://free.ishadowx.biz/"
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
        Html = requests.get(SSURL, headers=headers).text.replace('\r',
                                                                 '').replace(
                                                                     '\n', '')
        data = re.findall(
            r'<div class="col-sm-6 col-md-4 col-lg-4 ssr">(.*?)</div>', Html)
        for item in data:
            ip = re.findall(r'<span id="ipssr[a|c]">(.*?)</span>', item)
            port = re.findall(r'<span id="portssr[a|c]">(.*?)</span>', item)
            pwd = re.findall(r'<span id="pwssr[a|c]">(.*?)</span>', item)
            method = re.findall(r'Method:(.*?)<', item)
            hashs = re.findall(r'<h4>a(.*?)h</h4>', item)
            protocol = 'a' + str.split(hashs[0], ' ')[0]
            obfs = str.split(hashs[0], ' ')[1] + 'h'
            res = "{ip}:{port}:{protocol}:{method}:{obfs}:{pwdbase64}/?remarks={remarkbase64}".format(
                ip=ip[0],
                port=port[0],
                protocol=protocol,
                method=method[0],
                obfs=obfs,
                pwdbase64=(base64.b64encode(pwd[0].encode())).decode(),
                remarkbase64=(base64.b64encode('随便用'.encode())).decode())
            ssrlink = 'ssr://{0}'.format(
                (base64.b64encode(res.encode())).decode())
            SSRArr.append(ssrlink)
        return SSRArr

    def SaveFile(self, SSRURL):
        with open('SSR/SSR.txt', 'r+', encoding='utf-8') as f:
            f.seek(0)
            f.truncate()
        with open('SSR/SSR.txt', 'a', encoding='utf-8') as f:
            res = ''
            for data in SSRURL:
                res = res + data + '\n'
            result = (base64.b64encode((res).encode())).decode()
            f.write(result)