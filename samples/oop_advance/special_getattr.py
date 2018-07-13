#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

    def __init__(self):
        self.name = 'Michael'
#利用完全动态的__getattr__，我们可以写出一个链式调用
#只需要传入attr的名字，不需要每一个属性都写一个方法
#把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段
#当调用不存在的属性时，比如score，
#Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值
#动态获取属性的方法
    def __getattr__(self, attr):
        if attr=='score':
            return 99
        if attr=='age':
            #这里返回一个函数也是可以的
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

s = Student()
#s.name就是在调用属性！调用一个叫做name的属性！
print(s.name)
print(s.score)
#这里返回的是一个函数，所以必须s.age()
print(s.age())
# AttributeError: 'Student' object has no attribute 'grade'
print(s.grade)

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__
#chain就是建立了一个实例对象！不传值path取默认值''
#后面的.status.user.timeline.list 就是取属性对象这个对象叫做status.user.timeline.list，就这样打印出来了
Chain().status.user.timeline.list