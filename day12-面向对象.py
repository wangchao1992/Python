# -*-coding:utf-8 -*-
class Person:
    publicvar = 0 #  类型java中 public变量  这个没有下划线
    _protectvar=0 # 受保护类型 ，可以被继承  开头有一个下划线
    __privatevar=1 # 私有变量，只可以在本类使用 开头有两个下划线
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def say_Hi(self):
        print('hi ',self.name)
class Student(Person):#继承Person 。  支持多继承 ， 例 class Student(Person,Animal)：
    def __init__(self,name,age,stuNo):
        Person.__init__(self,name,age)
        self.stuNo = stuNo
        print(self._privatevar)
    def say_Hi(self):#重写say_hi()
        print('say_hi to {},in the Student'.format(self.name))

p = Person('xiaowang',23)
p.say_Hi()
print(p.name,p.age)

stu = Student('xiaoli',24,'110')
stu.say_Hi()
print(stu.name,stu.age,stu.stuNo)
print(p)
print(stu)