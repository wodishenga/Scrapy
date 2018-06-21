# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Dongguan.items import DongguanItem 

class DongguanspiderSpider(CrawlSpider):
    name = 'dongguanSpider'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ["http://wz.sun0769.com/index.php/question/questionType?type=4&page="]

    offset = 0
    start_urls = [url+str(offset)]
    def parse(self. response):
        #每一页里的所有帖子的链接集合
        links = response.xpath("//a[@class='new14']/@href")
        #迭代去除每一个帖子的链接
        for link in links:
                #提取每个帖子的链接，发送请求放到请求队列中，并调用self.parse_item处理
                yield scrapy.Request(link, callback=self.parse_item)
        if offset <= 71160:
                self.offset += 30
                #发送请求到请求队列中，调用self.parse处理response
                yield scrapy.Request(self.url+str(self.offset), callback=self.parse)

   #提取每一个帖子中的内容 
    def parse_item(self, response):
        item = DongguanItem()
        title = response.xpath('//div[@class="pagecenter p3"]//strong/text()').extract()[0]
        
        item["title"] = title
        item["number"] = title.split(":")[-1]
        item["url"] = response.url
        item["content"] = response.xpath('//div[@class="c1 text14_2"]/text()').extract()[0]
        
        yield item
