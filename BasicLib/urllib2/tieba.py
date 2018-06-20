#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2

def tiebaSpider(url, beginPage, endPage):
	"""
	作用：负责处理url，分配每个url去发送请求
	url：需要处理的第一个url
	beginPage: 爬虫执行的起始页面
	endPage: 爬虫执行的截止页面
	"""
	for page in range(beginPage, endPage+1):
		pn = (page - 1)*50
		filename = "第" + str(page) + "页.html"

		url = url+"&pn="+str(pn)
		#下载页面
		html = loadhtml(url, filename)
		#写入文件
		writehtml(html,filename)

def loadhtml(url, filename):
	'''
	作用：根据url发送请求，获取服务器响应文件
	url：需要爬取的url地址
	filename: 文件名
	'''
	print "正在下载" + filename
	headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0"}
		
	request = urllib2.Request(url, headers=headers)

	response = urllib2.urlopen(request)

	return response.read()

def writehtml(html, filename):
	"""
	作用：保存服务器响应文件到本地磁盘文件里
	html: 服务器响应文件
	filename: 本地磁盘文件名
	"""
	with open(filename, 'w') as f:
		f.write(html)

	print '-'*20


if __name__=="__main__":


	url = "https://tieba.baidu.com/f?"

	kw = raw_input("请输入需要爬取的贴吧:")
	# 输入起始页和终止页，str转成int类型
	beginPage = int(raw_input("请输入起始页："))
	endPage = int(raw_input("请输入终止页："))
	kw = {'kw':kw}

	# 通过urllib.urlencode() 参数是一个dict类型,转换成url编码格式（字符串）
	key = urllib.urlencode(kw)

	futureurl = url + key

	tiebaSpider(url, beginPage, endPage)




