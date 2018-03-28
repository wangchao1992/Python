#encoding=utf-8
f = open("telephones.txt",'r+')
tels = {}
content = f.read()
if len(content)>0:
    tels = eval(content)
print('{0:*^50}'.format('欢迎来到超哥私人定制的电话本'))
print('{}'.format(' 录入新联系人请按<1> '))
print('{}'.format(' 查询请按        <2> '))
print('{}'.format(' 退出请按        <3> '))
num = int(input())
while True:
    if num==1:
        print('请录入新的联系方式')
        name = input("请输入姓名：")
        tel = input("请输入电话：")
        tels[name]=tel
        num = int(input("请输入选项："))
    elif num==2:
        name = input("请输入要查询的姓名：")
        ishas = False
        for k in tels:
            if k==name:
                ishas = True
                print('{}的电话是{}'.format(name,tels[k]))
        if ishas==False:
            print("没有查到")
        num = input("请输入选项：")
    elif num==3:
        print('退出')
        break
    else:
        print("输入有误,请重新输入")
        num = int(input())
f.seek(0,0)
f.write(str(tels))
f.close()
