#coding=utf-8
#python version2.7
import urllib2
import urllib
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
           "Cookie":"BAIDUID=160B223E1AC173099FCFF4F57C2B87B3:FG=1; BIDUPSID=160B223E1AC173099FCFF4F57C2B87B3; PSTM=1522116900; BDSVRTM=0; BD_HOME=0; H_PS_PSSID=1434_13290_21116_20927"}
req = urllib2.Request("http://www.baidu.com",headers=headers)
req.add_header("Connection", "keep-alive") #也可以这样添加请求头。
# 也可以通过调用Request.get_header()来查看header信息
con = req.get_header(header_name="Connection")
print con
res = urllib2.urlopen(req)
print res.code
encodeurl = urllib.urlencode({"q":"你好吗？"})
print encodeurl
# print(res.read())

'''

'''
