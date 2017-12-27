# -*-coding:utf-8 -*-
'''
很多语言 都是以距离相近的一组大括号（{ }），称为一组代码块。
例：
if(isTrue){
    xxxx
    xxxx
}
在 Python 里 拥有相同缩进的代码行，称为一组代码块。
'''
# Python 里对缩进 要求是及其严格的。
i = 5
# 下面将发生错误，注意行首有一个空格， 把首行的空格删除再试试
 print('Value is',i)
print('I repeat, the value is', i)
