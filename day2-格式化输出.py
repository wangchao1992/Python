# -*-coding:utf-8 -*-
# 声明两个变量。 和其他语言不一样，完全不需要类型声明符。感觉像是在写伪代码。
age=23
name='chao'
#格式化输出字符串
print('{0}\'s age is {1} years old'.format(name,age))# 注意 字符串中 含有 ’ 需用 \ 转意符
#也可以这样，默认会按顺序填写
print('{}\'s age is {} years old '.format(name,age))

#格式化浮点数
print('{0:.3f}'.format(22/7.0)) # 保留3位小数

# 使用 * 填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '***hello***'字符串长度为 11
print('{0:*^11}'.format('hello'))
# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))