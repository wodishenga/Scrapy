# coding=utf-8


import scrapy
from mySpider.items import MyspiderItem


# 创建一个爬虫类
class ItcastSpider(scrapy.Spider):
    # 爬虫名字
    name = "itcast"
    # 允许爬虫作用的范围
    allow_domains = ["http://www.itcast.cn/"]

    # 爬虫起始的url
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml"]

    def parse(self, response):
        # with open("teacher.html","w") as f:
        #	f.write(response.body)
        # 我们将得到的数据保存到一个"mySpiderItem"对象中
        item = MyspiderItem()
        # 用scrapy自带的xpath匹配出列表集合
        teacher_list = response.xpath("//div[@class='li_txt']")

        #teacherItem = []
        for each in teacher_list:
            # #extract()方法返回的都是unicode字符串
            name = each.xpath("h3/text()").extract()
            title = each.xpath("h4/text()").extract()
            info = each.xpath("p/text()").extract()

            item["name"] = name[0]
            item["title"] = title[0]
            item["info"] = info[0]
	    #将获取的数据交给pipelines   
	    yield item
      #      teacherItem.append(item)
      #  return teacherItem


