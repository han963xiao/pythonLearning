#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools
#functools模块提供了很多有用的功能 下面讲的是偏函数的应用
#functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数
#将函数的参数固定化！
#前面是函数名，后面是默认值
int2 = functools.partial(int, base=2)

print('1000000 =', int2('1000000'))
print('1010101 =', int2('1010101'))
