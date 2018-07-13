#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
#例如函数执行之前的@log，很典型的装饰器，跟函数是独立的
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw) #这里就是原来的函数部分，即调用原来的函数
    return wrapper

#在定义函数的时候就有decorater，这样在运行的时候就运行两个独立的部分的，一个就是log里的部分，一个是now函数
#把@log放到now()函数的定义处，相当于执行了语句 now = log(now) @下面的函数作为变量，其实现在的now函数变了，变成了log(now)
#你要明白函数名其实就是一个指针，只是指向发生了改变

@log
def now():
    print('2015-3-25')

now()

#需要传入参数的decrator的写法，就要写三层！
#now = log('execute')(now) 首先执行log('execute')，返回的是decorator函数 我们上面那个decrator函数的名字叫做log
#
def logger(text): #这个text也是代指而已
    def decorator(func):
        @functools.wraps(func) #需要这一行的，自己看书根本留意不到的
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__)) #传入的参数在这里用到了
            return func(*args, **kw)
        return wrapper
    return decorator

@logger('DEBUG')
def today():
    print('2015-3-25')

today()
#每一个函数都存在很多属性，他们都是下划线开始的！向下面这些都使，每个函数都有
print(today.__name__)
print(today.__defaults__)