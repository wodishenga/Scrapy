#coding=utf-8

import urllib
import cookielib
from urllib2 import HTTPCookieProcessor,build_opener,Request

#通过cookieJar（）类创建的对象保存cookie的值
cookiejar = cookielib.CookieJar()


#构建处理器对象
handler = HTTPCookieProcessor(cookiejar)

#构建自定义opener
opener = build_opener(handler)

#人人网登录接口
url = "http://www.renren.com/PLogin.do"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0"}

#需要登陆的账户和密码
req_Data = {"email":"13265188722","password":"www268002108"}
data = urllib.urlencode(req_Data)

# 发送第一次的post请求，生成登录后的cookie(如果登录成功的话)
request = Request(url,data=data, headers=headers)

response = opener.open(request)

## 第二次可以是get请求，这个请求将保存生成cookie一并发到web服务器，服务器会验证cookie通过
response_img = opener.open('http://photo.renren.com/photo/966551112/albumlist/v7')
print response_img.read()
