# -*-coding:utf-8 -*-
site = 'http://www.baidu.com'
if site.startswith('http://'):
    print('this is netLocation')
if site.endswith('.com'):
    print('this is netLocation that end with com')
if 'baidu' in site:
    print('this is website about baidu')
if site.find('bai')!=-1:
    print('Yes,it contains the string \"bai\"')
#  join 字符串 和 分解字符串
delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))
a = delimiter.join(mylist).split('_*_')
print(a)
