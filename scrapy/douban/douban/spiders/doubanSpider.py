# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

class DoubanspiderSpider(scrapy.Spider):
    name = 'doubanSpider'
    allowed_domains = ['douban.com']
    url = 'https://movie.douban.com/top250?start='
    offset = 0
    endurl = '&filter='
    start_urls = [url+str(offset)+endurl]
    
    def parse(self, response):
        
        item = DoubanItem()
        movies = response.xpath("//div[@class='info']")
        
        for movie in movies:
            #名称
            item["moviename"] = movie.xpath(".//span[@class='title'][1]/text()").extract()[0]
            #信息
            #movieinfo = movie.xpath(".//div[@class='bd']/p/text()").extract()
            item["movieinfo"] = movie.xpath(".//div[@class='bd']/p/text()").extract()[0]
            #for info in movieinfo:
             #   item["movieinfo"] = ";".join(info)
            #评分
            item["moviescore"] = movie.xpath(".//div[@class='star']/span[2]/text()").extract()[0]
            #评价
            comment = movie.xpath(".//p[@class='quote']/span/text()").extract()
            if len(comment) != 0:
                item["moviecomment"] = comment[0]
            yield item
        if self.offset < 225:
            self.offset += 25
            yield scrapy.Request(self.url+str(self.offset)+self.endurl, callback = self.parse)
