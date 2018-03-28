class Person:
    num = 0
    def __init__(self,new_num):
        Person.num+=1
        self.num = new_num
    def hello(self):
        print('hello world')


p3 = Person(50)
p4 = Person(100)

print(p3.num)
print(p4.num)
print(Person.num)
print(p3.__dict__)