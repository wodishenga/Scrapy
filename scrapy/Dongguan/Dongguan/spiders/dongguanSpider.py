# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Dongguan.items import DongguanItem 

class DongguanspiderSpider(CrawlSpider):
    name = 'dongguanSpider'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ["http://wz.sun0769.com/index.php/question/questionType?type=4&page="]

    rules = (
        Rule(LinkExtractor(allow=r'type=4&page=\d+'), follow=True),
        Rule(LinkExtractor(allow=r'/question/\d+/\d+.shtml'), follow=True, callback="parse_item"),
    )
    
    def parse_item(self, response):
        item = DongguanItem()
        title = response.xpath('//div[@class="pagecenter p3"]//strong/text()').extract()[0]
        
        item["title"] = title
        item["number"] = title.split(":")[-1]
        item["url"] = response.url
        item["content"] = response.xpath('//div[@class="c1 text14_2"]/text()').extract()[0]
        
        yield item
