from Scrapy_SS import SS

if __name__ == "__main__":
    res = SS()
    lists = res.GetHtmlText()
    byte = res.QrCode(lists)
    res.SaveFile(byte)
