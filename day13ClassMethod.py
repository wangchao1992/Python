#coding=utf-8
class Person(object):
    name = "Person"#定义类属性
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @classmethod
    def classmethod(cls):
        print(cls)
        print(cls.name)

p = Person("wangchao",12)
p.classmethod()
Person.classmethod()
print(Person.name) #访问类属性
print(p.name)#访问实例属性