#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能
#可以只给一个对象绑定方法！只对这个对象有用
#也可以给一个类绑定方法！对类创建的全体对象都有用
class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
#Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
#_slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的,因此下面给GraduateStudent附属性是可以的

class GraduateStudent(Student):
    pass

#下面是只给一个对象绑定了方法
s = Student() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'
# ERROR: AttributeError: 'Student' object has no attribute 'score'
try:
    #因为__slots__的作用不能绑定score这个属性,试图绑定score将得到AttributeError的错误
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)

g = GraduateStudent()
g.score = 99
print('g.score =', g.score)
