#coding=utf-8

import urllib2



ua_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

#通过urllib2.Request() 方法构造一个请求对象
request = urllib2.Request("http://www.baidu.com/", headers = ua_headers)


# 向指定的url地址发送请求，并返回服务器响应的类文件对象
response = urllib2.urlopen(request)

html = response.read()

# 返回 HTTP的响应码，成功返回200，4服务器页面出错，5服务器问题
print response.getcode()

# 返回 返回实际数据的实际URL，防止重定向问题
print response.geturl()

# 返回 服务器响应的HTTP报头
print response.info()



