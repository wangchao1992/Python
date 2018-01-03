# -*-coding:utf-8 -*-
'''
当你创建了一个对象并将其分配给某个变量时，变量只会查阅（Refer）某个对象，并且它也
不会代表对象本身。也就是说，变量名只是指向你计算机内存中存储了相应对象的那一部
分。这叫作将名称绑定（Binding）给那一个对象。
一般来说，你不需要去关心这个，不过由于这一引用操作困难会产生某些微妙的效果，这是
需要你注意的：
'''
print('Simple Assignment')
shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist 只是指向同一对象的另一种名称
mylist = shoplist
# 我购买了第一项项目，所以我将其从列表中删除
del shoplist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)
# 注意到 shoplist 和 mylist 二者都 打印出了其中都没有 apple 的同样的列表，
# 以此我们确认它们指向的是同一个对象
print('Copy by making a full slice')
# 通过生成一份完整的切片制作一份列表的副本
#mylist = shoplist[:] # 注意 这样会创建一个副本
mylist = shoplist.copy() # 这一也可以创建一个副本。删除副本中的元素将不会影响 原来的元素
# 删除第一个项目
del mylist[0]
print('shoplist is', shoplist)
print('mylist is', mylist)
# 注意到现在两份列表已出现不同



'''
你要记住如果你希望创建一份诸如序列等复杂对象的副本（而非整数这种简单的对象
（Object）），你必须使用切片操作来制作副本。如果你仅仅是将一个变量名赋予给另一个名
称，那么它们都将 (引用)“refer”同一个对象，如果你对此不够小心，那么它将造成麻烦。
'''