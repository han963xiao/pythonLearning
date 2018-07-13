#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#返回函数
#高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
#这个没有弄懂有什么用，先粗略看一遍把，用到再回来看
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
#你看定义的这个sun返回的不是一个值，而是一个函数，里面的sum函数实现了累加功能，返回的就是sum函数
#我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）

#当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
# f1 = lazy_sum(1, 3, 5, 7, 9) 这两个完全不一样的，每次创造出一个新对象
# f2 = lazy_sum(1, 3, 5, 7, 9)
f = lazy_sum(1, 2, 4, 5, 7, 8, 9)
print(f)
print(f())

# why f1(), f2(), f3() returns 9, 9, 9 rather than 1, 4, 9?
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i * i
        fs.append(f)
    return fs
#原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
#
f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())

# fix:
def count():
    fs = []
    def f(n):
        def j():
            return n * n
        return j
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())
