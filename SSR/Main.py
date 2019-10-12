import requests
import json

SSRApi = "https://lncn.org/api/lncn"


def GetSSR():
    result = requests.post(SSRApi).text
    dic = json.loads(result)
    return dic.get("ssrs")


def SaveSSR():
    sub = GetSSR() #目前还需要解密
    with open('SSR/SSR.txt', 'r+', encoding='utf-8') as f:
        f.seek(0)
        f.truncate()
    with open('SSR/SSR.txt', 'a', encoding='utf-8') as f:
        f.write(sub)
        f.write('\n')


if __name__ == "__main__":
    SaveSSR()