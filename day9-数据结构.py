# -*-coding:utf-8 -*-
'''
数据结构（Data Structures）基本上人如其名——它们只是一种结构，能够将一些数据聚合
在一起。换句话说，它们是用来存储一系列相关数据的集合。
Python 中有四种内置的数据结构——列表（List）、元组（Tuple）、字典（Dictionary）和集
合（Set）。我们将了解如何使用它们，并利用它们将我们的编程之路变得更加简单。
个人总结：数据结构就是数组存储的一种结构。每种结构都有自己的特点
'''
# ----------------------list 列表-------------------
# 列表 是存储一组 数据的 数据结构。 可对列表，添加 ，修改，删除， 因此 它相当灵活 ，是一种可变的序列
shoplist = ['apple', 'mango', 'carrot', 'banana']
shoplist.append('rice')#追加元素
print(shoplist)
shoplist.sort() #排序
print(shoplist)
del shoplist[0]# 删除列表第一个元素
print(shoplist)
shoplist.append(1)# 可以向列表中 添加 数字，list ，对象
shoplist.append(['a',print()])
print(shoplist) # 列表 也是一种序列 ，可以用 for 循环遍历
for i in shoplist:
    print(i)
# ------------ Tuple 元组--------------
# 元组 和列表 很相似， 但元组没有 修改， 添加，删除 元素的功能，所以他是不可变的序列
tuple = ('python','elephant','penguin')
print('tuple\'s len is ',len(tuple))#  输出元组的长度。
new_zoo = 'monkey','camel',tuple
print(new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is',
len(new_zoo)-1+len(new_zoo[2]))
# 遍历 元组里的内容
for i in new_zoo:
    print(i)
print((2)) # 这是一个数字 2
print((2,)) # 这是只有一个元素 （2） 的 元组，
#------------------------- dict 字典 ------------------------
# “ab”是地址（Address）簿（Book）的缩写
ab = {
'Swaroop': 'swaroop@swaroopch.com',
'Larry': 'larry@wall.org',
'Matsumoto': 'matz@ruby-lang.org',
'Spammer': 'spammer@hotmail.com'
}
print("Swaroop's address is", ab['Swaroop'])
# 删除一对键值—值配对
del ab['Spammer']
print('\nThere are {} contacts in the address-book\n'.format(len(ab)))
for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))
# 添加一对键值—值配对
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])
# ------------------------------切片
print('{0:*^50}'.format('切片'))
shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[-1])
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])
print('xxxx', name[::-1])
#========================  集合 -=-=-==-=-=-=-=-=-=-=-=-====
print('{0:*^50}'.format('集合'))
bri = set(['brazil','russia','india'])
print('india'in bri)
bric = bri.copy()
bric.add('china')
bric.remove('russia')
print(bric.issuperset(bri)) # 是否是目标对象的父集
# 取交集
print(bri.intersection(bric))


