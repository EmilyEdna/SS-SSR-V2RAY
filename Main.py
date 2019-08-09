import Scrapy

if __name__ == "__main__":
    res = Scrapy.SS()
    lists = res.GetHtmlText()
    byte = res.QrCode(lists)
    res.SaveFile(byte)
