#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import time 

def captcha(captcha_data):
	with open("captcha.jpg", "wb") as f:
		f.write(captcha_data)
	text = raw_input("请输入验证码：")
    	# 返回用户输入的验证码
    	return text


def zhihuLogin():

	#构建session对象，保存cookie
	sess = requests.Session()

	 # 请求报头
    	headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}


	#获取登录界面，找到需要post的数据，同时记录当前的cookie
	html = sess.get("https://www.zhihu.com/#signin",headers=headers).text

	# 调用lxml解析库
	bs = BeautifulSoup(html, 'lxml')

	# 找到name属性值为 _xsrf 的input标签，再取出value 的值
	_xsrf = bs.find("input", attrs={"name":"_xsrf"}.get("value"))

	#破解验证码
	# 根据UNIX时间戳，匹配出验证码的URL地址
    	captcha_url = "https://www.zhihu.com/captcha.gif?r=%d&type=login" % (time.time() * 1000)
    	# 发送图片的请求，获取图片数据流，
    	captcha_data = sess.get(captcha_url, headers = headers).content
   	 # 获取验证码里的文字，需要手动输入
    	text = captcha(captcha_data)

	#发送登录需要的post数据，获取登录后的cookie
	data = {
        "_xsrf" : _xsrf,
        "email" : "123636274@qq.com",
        "password" : "ALARMCHIME",
        "captcha" : text
    	}
 	response = sess.post("https://www.zhihu.com/login/email", data = data, headers = headers)
	#用已有登录状态的Cookie发送请求，获取目标页面源码
 	response = sess.get("https://www.zhihu.com/people/zhu/activities", headers = headers)
    	with open("my.html", "w") as f:
        f.write(response.text.encode("utf-8"))

        
if __name__ == "__main__":
    	zhihuLogin()
