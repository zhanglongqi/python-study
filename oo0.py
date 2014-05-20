# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 16:28:27 2013

@author: longqi
"""
class Person(object):
	count = 0
	#name = ''
	def __init__(self,name):
		Person.count += 1
		self.number = Person.count
		self.name = name
	def sayHi(self):
		print "Hello,I'm",self.name,",No.",self.number,", We have ",Person.count
#self.sayHi()
	def setAge(self,age):
		self.age = age

print Person,type(Person)

p = Person("longqi")
p2 = Person("C-3PO")
p3 = Person("R2-D2")

print p,type(p)

p.sayHi()
p2.sayHi()
p3.sayHi()
#Person().sayHi()
Person("The Dark One").sayHi()


print "*************inheritance**************"

class Teacher(Person):
	def __init__(self,name,age):
		Person.__init__(self,name)#必须手动调用父类构造函数
		self.age=age
	def sayHi(self):
		Person.sayHi(self)
	#	super(Teacher, self).sayHi()

t=Teacher("T1",32)
t.sayHi()
print "type of teacher t1",type(t)
print issubclass(t.__class__,object)
print isinstance(t, object)
# new-style classes or old-style calss ?
#http://stackoverflow.com/questions/9698614/super-raises-typeerror-must-be-type-not-classobj-for-new-style-class
def is_new_style_class(klass):
    return issubclass(klass, object)

def is_new_style_class_instance(instance):
    return isinstance(instance, object)

def is_new_style_class2(klass):
    try:
        return issubclass(klass, object)
    except TypeError:
        return False
