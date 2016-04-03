__author__ = "Vicx"

import scrapy

from newspider.items import NewspiderItem

class QiuBaiSpider(scrapy.Spider):
    name = "qiubai"
    start_urls = [
        "http://www.qiushibaike.com/",
    ]

    def parse(self, response):
        pattern1 = '//div[@class = "article block untagged mb15"]'
        pattern2 = './div[@class = "author clearfix"]/a[2]/h2/text()'
        pattern3 = './div[@class = "content"]/text()'
        for ele in response.xpath(pattern1):
            authors = ele.xpath(pattern2).extract()
            contents = ele.xpath(pattern3).extract()

            yield NewspiderItem(author=authors,content=contents)






