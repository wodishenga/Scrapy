#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib
import urllib2


url = "https://www.baidu.com/s"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0"}

keyword = raw_input('请输入关键字:')
wd = {'wd':keyword}

# 通过urllib.urlencode() 参数是一个dict类型
wd = urllib.urlencode(wd)

futureurl = url+ "?" + wd


request = urllib2.Request(futureurl, headers = headers)

response = urllib2.urlopen(request)

print response.read()

