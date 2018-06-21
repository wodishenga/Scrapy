# -*- coding: utf-8 -*-
import scrapy


#只要是需要提供post数据的，就可以用这种方法
class RenrenSpider(scrapy.Spider):
    """直接POST数据（比如需要登陆的账户信息)"""
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/PLogin.do']
    
    def start_requests(self):
	url = "http://www.renren.com/PLogin.do"
	#FormRequest是scrapy发送Post请求的方法
	yield scrapy.FormRequest(
		url = url,
		formdata =  {"email" : "1577726407@qq.com", "password" : "XXXXX"},
		callback = self.parse_page,
	)

    def parse_page(self, response):
	with open("hah.html", "w") as filename:
            filename.write(response.body)
