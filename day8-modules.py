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
# 使用 dir（） 函数查看，一个类内部的变量及方法 ， 参数是要查看类的名字， 如果不传 是当前类
a =5
print(dir())
del a
print(dir())# 发现 a  不见了
print(dir(sqrt))
# 包
'''
现在，你必须开始遵守用以组织你的程序的层次结构。变量通常位于函数内部，函数与全局
变量通常位于模块内部。如果你希望组织起这些模块的话，应该怎么办？这便是包
（Packages）应当登场的时刻。
包是指一个包含模块与一个特殊的  __init__.py  文件的文件夹，后者向 Python 表明这一文
件夹是特别的，因为其包含了 Python 模块。
建设你想创建一个名为“world”的包，其中还包含着 ”asia“、”africa“等其它子包，同时这些子
包都包含了诸如”india“、”madagascar“等模块。
'''
# 下面是你会构建出的文件夹的结构：
'''
- <some folder present in the sys.path>/
    - world/
        - __init__.py
        - asia/
              - __init__.py
              - india/
                  - __init__.py
                  - foo.py
        - africa/
              - __init__.py
              - madagascar/
                 - __init__.py
                 - bar.py
包是一种能够方便地分层组织模块的方式。你将在 标准库 中看到许多有关于此的实例。
'''
'''
总结
如同函数是程序中的可重用部分那般，模块是一种可重用的程序。包是用以组织模块的另一
种层次结构。Python 所附带的标准库就是这样一组有关包与模块的例子。
我们已经了解了如何使用这些模块并创建你自己的模块。
'''