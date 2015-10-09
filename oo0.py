# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 16:28:27 2013

@author: longqi
"""


class Person(object):
    count = 0
    # name = ''

    def __init__(self, name):
        Person.count += 1
        self.number = Person.count
        self.name = name
        self.age = -1

    def say_hi(self):
        print("Hello, I'm", self.name, ", No.", self.number, ", We have ", Person.count, '\n')
        # self.sayHi()

    def set_age(self, age):
        self.age = age


print(111111111111111)
print(Person, type(Person))

p = Person("longqi")
p2 = Person("C-3PO")
p3 = Person("R2-D2")

print(2222222222222222)
print(p, type(p))

print(333333333333333)
p.set_age(5)
print(p.age)
p.say_hi()

p2.say_hi()
print(p2.age)
p3.say_hi()
Person("").say_hi()
Person("The Dark One").say_hi()

print("*************inheritance**************", "\n")


class Teacher(Person):
    def __init__(self, name, age):
        Person.__init__(self, name)  # 必须手动调用父类构造函数
        self.age = age

    def say_hi(self):
        Person.say_hi(self)
        #    super(Teacher, self).say_hi()


t = Teacher("T1", 32)
t.say_hi()
print("type of teacher t1", type(t))
print(issubclass(t.__class__, object))
print(isinstance(t, object))


# new-style classes or old-style class ?
# http://stackoverflow.com/questions/9698614/super-raises-typeerror-must-be-type-not-classobj-for-new-style-class


def is_new_style_class(klass):
    return issubclass(klass, object)


def is_new_style_class_instance(instance):
    return isinstance(instance, object)


def is_new_style_class2(klass):
    try:
        return issubclass(klass, object)
    except TypeError:
        return False
