# python version 2.7
import urllib2
req = urllib2.Request("http://www.baidu.com")
res = urllib2.urlopen(req)
print(res.code) # 打印状态码
print(res.read())# 打印响应体