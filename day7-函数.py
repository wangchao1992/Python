# -*-coding:utf-8 -*-
'''
函数（Functions）是指可重复使用的程序片段。
函数可以通过关键字  def  来定义。

'''
# -------------------------无参数  函数--------------------------
def say_hello():
    print('hello world')

say_hello()
# ---------------------------有参数 函数-------------------------------
def say_hello_to(name):
    print('hello ',name)
say_hello_to('chao')
# ---------------------------函数默认值------------------------------
# 带有默认值 的参数，必须在参数列表的末尾。
#  因为值是按参数所处的位置依次分配的。举例来说， def func(a, b=5)  是有效的，
# 但  def func(a=5, b)  是无效的
def say(name,age=10):
    print('{}\'s age is {}. '.format(name,age))
say('chao') # 第二个参数 age，不传默认是 10
say('chao',23)
# 也可以通过关键字 传递参数， 这样是不分先后顺序的。
# 必须把没有默认值的参数都写全，否则会报错
say(age=25,name='chao')
#----------------------------可变参数---------------------------------
'''
有时你可能想定义的函数里面能够有任意数量的变量，也就是参数数量是可变的，这可以通过使用星号来实现

'''
print('{0:*^50}'.format('可变参数'))
def total(a=5, *numbers, **phonebook):
    print('a', a)
    #遍历元组中的所有项目
    for single_item in numbers:
        print('single_item', single_item)
    #遍历字典中的所有项目
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)
print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))
'''
它是如何工作的
当我们声明一个诸如  *param  的星号参数时，从此处开始直到结束的所有位置参数
（Positional Arguments）都将被收集并汇集成一个称为“param”的元组（Tuple）。
类似地，当我们声明一个诸如  **param  的双星号参数时，从此处开始直至结束的所有关键字
参数都将被收集并汇集成一个名为  param  的字典（Dictionary）。
'''
#----------------------------函数返回值------------------------------
def maximum(x,y):
    if x>y:
        return x
    elif x<y:
        return y
    else:
        return 'The numbers are equal'
print(maximum(5,-19))
#再看一下这个例子
def some_fun():
    '''
    This is some_fun's docString.
       函数的第一行逻辑行中的字符串是该函数的 文档字符串（DocString）。
        该文档字符串所约定的是一串多行字符串
        文档字符串主要要来 描述函数的参数定义，以及如何使用函数。
        强烈建议在开发中写DocString
       '''
    pass
print(some_fun())
# Python 中的  pass  语句用于指示一个没有内容的语句块
# 每一个函数都在其末尾隐含了一句  return None  ，除非你写了你自己的  return  语句
print(some_fun.__doc__)
print(print.__doc__)# 看一下系统的 文档字符串怎么写