#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# type()
#判断对象类型，使用type()函数
print('type(123) =', type(123))
print('type(\'123\') =', type('123'))
print('type(None) =', type(None))
#<class 'builtin_function_or_method'> 表示这个是函数或者方法，函数function意思就是可以直接使用，method就是必须有对象从才可以使用
print('type(abs) =', type(abs))

import types

print('type(\'abc\')==str?', type('abc')==str)

