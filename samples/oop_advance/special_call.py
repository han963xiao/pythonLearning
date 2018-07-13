#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#一个对象实例可以有自己的属性和方法，
# 当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的
#例如建立一个对象a a.method就是使用对象中的方法
#__call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，
#所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别
#你建立了一个student对象叫做a 然后a()就是调用了他里面的__call__方法！student对象中的这个方法！
#其实就是把对象当做函数用了

class Student(object):
    #初始化的方法！
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('Michael')
#定义一个__call__()方法，就可以直接对实例进行调用
s()
