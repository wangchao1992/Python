# encoding=utf-8

import random

# 定义一个列表用来保存3个办公室
offices = [[],[],[]]

# 定义一个列表用来存储8位老师的名字
names = ['A','B','C','D','E','F','G','H']

for name in names:
    index = random.randint(0,2)
    offices[index].append(name)
print(offices)
i=0
for office in offices:
    print("办公室{}号有{}个员工".format(i,len(office)))
    for person in office:
        print(person,end="")
    print("\n")
    i+=1
a = ('a','b','c','a','b')
print()