__author__ = "Vicx"

import scrapy
from scrapy.http import Request


from newspider.items import NewspiderItem

class QiuBaiSpider(scrapy.Spider):
    name = "qiubai"
    start_urls = [
        "http://www.qiushibaike.com/",
    ]

    def parse(self, response):

        for href in response.xpath('//span[@class="stats-comments"]/a/@href').extract():
            detail_url = response.urljoin(href)
            req = Request(detail_url,self.parse_detail_page)

            item = NewspiderItem()
            req.meta["item"] = item
            yield req

    def parse_detail_page(self,response):

        pattern1 = '//div[starts-with(@class,"comment-block clearfix floor")]'
        pattern2 = '//div[@class = "author clearfix"]/a[2]/h2/text()'
        pattern3 = '//div[@class = "content"]/text()'

        item = response.meta["item"]
        item["author"] = response.xpath(pattern2).extract()[0]
        item["content"] = response.xpath(pattern3).extract()[0]
        comments = []
        for comment in response.xpath(pattern1):
            comment_author = comment.xpath('./div[2]/a/text()').extract()[0]
            comment_content = comment.xpath('./div[2]/span/text()').extract()[0]

            comments.append({"comment_author":comment_author,"comment_content":comment_content})

        item["comments"] = comments
        yield  item











