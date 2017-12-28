# -*-coding:utf-8 -*-
#-------------- 局部变量 ------------------
x = 50
def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)
func(x)
print('x is still', x)
# 发现没有，在函数内部修改 x = 2 ,对外边的变量没有影响

#-------------- 全局变量 ------------------
print('{0:*^50}'.format('global'))
x = 50
def func(x):
    print('x is', x)
    global x1
    global y, z
    z=y=100 # 一次给多个变量赋值
    x1=x
    print('Changed x1 to', x)
func(x)
print('x1 is still', x1)
print('y = {},z = {}'.format(y,z))
#发现没有，  x1 ,y,z 定义在函数内部 ，在函数外部也可以调用

