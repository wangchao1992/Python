#-*-coding=utf-8-*-
# python version-2.7
import urllib
import urllib2

#http://tieba.baidu.com/f?kw=%E7%BB%9D%E5%9C%B0%E6%B1%82%E7%94%9F&ie=utf-8&pn=0
def tiebaSpider(url,beginNum,endNum):
    for page in range(beginNum,endNum+1,1):
        page = (page-1)*50
        url = url+"&pn="+str(page)
        html = getHtml(url)
        fileName= ""+str(page)+".html"
        writeFile(html,fileName)
def getHtml(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    return response.read()
def writeFile(html,filename):
    print "正在存储" + filename
    with open(filename,'w') as f:
        f.write(html)
    #print html


if __name__=="__main__":
    kw = raw_input("请输入要爬的贴吧主题：")
    begin = int(raw_input("请输入起始页"))
    end = int(raw_input("请输入终止页："))
    url = 'http://tieba.baidu.com/f'

    param = urllib.urlencode({'kw':kw,
                        'ie':'utf-8'
                         })
    url = url+'?'+param
    tiebaSpider(url,begin,end)

