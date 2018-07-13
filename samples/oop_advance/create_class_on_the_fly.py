#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#type函数对应jaca中的class很强大的！

def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class

h = Hello()
print('call h.hello():')
h.hello()
#type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type
print('type(Hello) =', type(Hello))
#而h是一个实例，它的类型就是class Hello
print('type(h) =', type(h))

# Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
#可以像上面这样动态的创立hello CLASS，根本不需要定义hello CLASS
#要创建一个class对象，type()函数依次传入3个参数：
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；(object,)
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上
# h = Hello() 还是创立一个对象
# h.hello() 跟h.fn()是一样的 第三个参数的方法
