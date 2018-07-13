#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#高级语言通常都内置了一套try...except...finally...的错误处理机制，Python也不例外
#应该由不同的except语句块处理。没错，可以有多个except来捕获不同类型的错误
#java是try catch python是try except
#Python的错误其实也是class，所有的错误类型都继承自BaseException

try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')
