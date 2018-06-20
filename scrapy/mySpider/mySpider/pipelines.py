# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class MyspiderPipeline(object):
    # __init__方法是可选的，做为类的初始化方法
    def __init__(self):
        #创建一个文件
	self.filename = open("teacher.json","w")

    def process_item(self, item, spider):
        # process_item方法是必须写的，用来处理item数据
        jsontext = json.dumps(dict(item), ensure_ascii = False) + '\n'
        self.filename.write(jsontext.encode("utf-8"))
        return item

    def close_spider(self,spider):
        ## close_spider方法是可选的，结束时调用这个方法
        self.filename.close()
    
    
