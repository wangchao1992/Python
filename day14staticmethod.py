#coding = utf-8
name = 100 #这个变量只能静态方法访问
class Person(object):
    name = "Person"#定义类属性
    def __init__(self,name,age):
        self.name = name
        self.age = age
    @staticmethod
    def staticmethod():
        print(name)

p = Person("wangchao",12)

p.staticmethod()
Person.staticmethod()
print(Person.name) #访问类属性
print(p.name)#访问实例属性
