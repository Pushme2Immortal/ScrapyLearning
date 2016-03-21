__author__ = "Vicx"

import scrapy

class QiuBaiSpider(scrapy.Spider):
    name = "qiubai"
    start_urls = [
        "http://www.qiushibaike.com/",
    ]

    def parse(self, response):
        tmp = response.xpath('//div[@class="author clearfix"]/a/@title').extract()
        for x in tmp:
            print x.encode("utf-8")



