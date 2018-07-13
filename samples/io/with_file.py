#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#现代操作系统不允许普通的程序直接操作磁盘，所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符）
# 然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）
from datetime import datetime

#后面的w是以什么方式打开这个txt，w代表是以写的方式，后面r是以读的方式

#Python引入了with语句来自动帮我们调用close()方法
#这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法，会自动帮我们调用close方法

#调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，
# 调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用

#如果文件很小，read()一次性读取最方便；
# 如果不能确定文件大小，反复调用read(size)比较保险；
# 如果是配置文件，调用readlines()最方便

#先withopen 得到文件映像 后面是读还是写都可以的.read()或者.write()
#传入标识符'w'或者'wb'表示写文本文件或写二进制文件
#细心的童鞋会发现，以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。
# 如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入
with open('test.txt', 'w') as f:
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y-%m-%d'))

with open('test.txt', 'r') as f:
    s = f.read()
    print('open for read...')
    print(s)

#前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。
# 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
with open('test.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)

#要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件
# with open('/user/michael/gbk.tst','r',encoding='gbk',errors='ignore')as f: