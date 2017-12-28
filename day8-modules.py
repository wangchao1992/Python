'''
如果你想在你所编写的别的程序中重用一些函数的话，应该怎么办？
正如你可能想象到的那样，答案是模块（Modules）。
编写模块有很多种方法，其中最简单的一种便是创建一个包含函数与变量、以  .py  为后缀的文件。
所以我们写的每个 以 .py 为后缀的 文件 都是一个模块， 注意 文件名不能含有中文。
'''
import sys
print('The command line arguments are:')
for i in sys.argv:
    print(i)
print('\n\nThe PYTHONPATH is ',sys.path,'\n')
'''
from..import  语句
如果你希望直接将  argv  变量导入你的程序（为了避免每次都要输入  sys.  ），那么你可以
通过使用  from sys import argv  语句来实现这一点。
警告：一般来说，你应该尽量避免使用  from...import  语句，而去使用  import  语句。
这是为了避免在你的程序中出现名称冲突，同时也为了使程序更加易读。
'''
# 例
from math import sqrt
print("Square root of 16 is", sqrt(16))
#每个模块都有一个名称，而模块中的语句可以找到它们所处的模块的名称。
# 这对于确定模块是独立运行的还是被导入进来运行的这一特定目的来说大为有用
# 例
if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')