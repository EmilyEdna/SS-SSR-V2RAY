from Scrapy_V2ray import V2RAY

if __name__ == "__main__":
    res = V2RAY()
    vmess = res.GetHtmlText()
    res.SaveFile(vmess)
