#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#很多时候，数据读写不一定是文件，也可以在内存中读写
# StringIO顾名思义就是在内存中读写str。
# 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可
from io import StringIO

# write to StringIO:

#创立了一个stringIO的对象！往里面写入了
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')

#stringIO的对象里面取值
print(f.getvalue())

# read from StringIO:

#在建立的时候就把要用的字符串输进去！！！
f = StringIO('水面细风生，\n菱歌慢慢声。\n客亭临小市，\n灯火夜妆明。')

#每一次读一行！！
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
