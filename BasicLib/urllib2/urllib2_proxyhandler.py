#coding=utf-8

import urllib2

proxyswitch=True

# 构建一个Handler处理器对象，参数是一个字典类型，包括代理类型和代理服务器IP+PROT
proxy_handler = urllib2.ProxyHandler({"http":"122.72.18.35:80"})
noproxy_handler = urllib2.ProxyHandler({})  #没有代理


if proxyswitch:
	opener = urllib2.build_opener(proxy_handler)
else:
	opener = urllib2.build_opener(noproxy_handler)


# 构建了一个全局的opener，之后所有的请求都可以用urlopen()方式去发送，也附带Handler的功能
urllib2.install_opener(opener)

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
request = urllib2.Request("http://www.baidu.com/", headers=headers)

response = urllib2.urlopen(request)

print response.read()



