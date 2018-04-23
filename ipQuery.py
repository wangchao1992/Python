#coding=utf-8
#Python version 2.7
import urllib2
import urllib
import json
import jsonpath
import sys
def query(ip):
        url = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query={}&co=&resource_id=6006&ie=utf8&oe=gbk&cb=op_aladdin_callback&format=json'
        req = urllib2.Request(url=url.format(ip))
        response = urllib2.urlopen(req).read()
        start = '/**/op_aladdin_callback('.__len__()
        jsonstr = json.loads(response[start:-2],encoding='gbk')
        location = jsonpath.jsonpath(jsonstr,'$..location')[0]
        print location
        #print location.encode('utf-8')
if __name__ == '__main__':
         ip = sys.argv[1]
         query(ip)

