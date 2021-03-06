# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    #电影名称
    moviename = scrapy.Field()
    #电影信息
    movieinfo = scrapy.Field()
    #电影评分
    moviescore = scrapy.Field()
    #电影评价
    moviecomment = scrapy.Field()
