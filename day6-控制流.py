# -*-coding:utf-8 -*-
# 在 Python 中有三种控制流语句—— if   for  和  while  。
# Python 中不存在switch 语句。
#---------------------------if 语句-------------------------------------------
number = 23
guess = int(input('Enter an integer :'))
if guess ==  number:
    # 新代码块从这里开始
    print('Congratulations,you guessed it')
    print('(but you do not win any prizes!)')
    # 新代码块到这里结束
elif guess < number:
    # 另一个代码块
    print('No,it is a little higher than that')
    # 你可以在此做任何你希望在该代码块内进行的事情
    # 缩进必须相同
elif guess > number:
    print('No,it is a little lower than that')
else:
    # else 可以省略
    print('什么也不做')
print('Done')
# ------------------------------------while 语句-------------------------------------------------------
'''
while  语句能够让你在条件为真的前提下重复执行某块语句。  while  语句是 循环
（Looping） 语句的一种。 while  语句同样可以拥有  else  子句作为可选选项。
可用 break 提前结束循环
'''
number = 23
running = True # True  False 也可以将它们分别等价地视为  1  与  0
while running:
    guess = int(input('Enter an integer : '))
    if guess == number:
        print('Congratulations, you guessed it.')
        # 这将导致 while 循环中止
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
else:
    print('The while loop is over.')
# 在这里你可以做你想做的任何事
print('Done')
print(guess)
# 发现没有，Python好像没有作用域区分
# ----------------------------- for 循环 ------------------------------------------------
'''
for 循环也支持  else
for 循环支持 break 提前结束
'''
for i in range(1,5): # 猜猜执行了几次。 4次， [1,2,3,4] 不包括 5
    print(i)
   # break
else:
    print('The for loop is over')
#-------------------- break 语句  continue 语句 ---------------------------
'''
break 语句可提前结束 while 或 for 循环 
continue  语句可以跳过当前循环块中的剩余语句，并继续该循环的下一次迭
代。
'''
while True:
    s = input('Enter something : ')
    # 直到输入 quit 才会退出。
    if s == 'quit':
        break
    if len(s<3):
        print('Too small')
        continue
    print('Length of the string is', len(s))
print('Done')