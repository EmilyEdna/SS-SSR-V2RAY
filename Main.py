import Scrapy_SS

if __name__ == "__main__":
    res = Scrapy_SS.SS()
    lists = res.GetHtmlText()
    byte = res.QrCode(lists)
    res.SaveFile(byte)
