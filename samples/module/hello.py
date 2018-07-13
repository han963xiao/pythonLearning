#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '
#紧接着注释的第一个字符串就是该文档的注释
#任何模块代码的第一个字符串都被视为模块的文档注释
__author__ = 'Michael Liao'
#python里每一个函数，每一个类的属性都是__name__ 这种形式的
#上面这些就是标注文件模板，可以全部删掉不谢，但是按标注办事肯定没错


import sys
#导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能
#所有的名字都是指针的，sys就是指向模块的指针变量
#这里讲模块化的应用，如何使用模块和安装第三方模块
#定义了一个函数
#ys模块有一个argv变量，用list存储了命令行的所有参数。
# argv至少有一个元素，因为第一个参数永远是该.py文件的名称

def test():
    args = sys.argv #里面有一个变量叫做argv
    if len(args)==1:
            print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

#模块化的规范
#类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量
#类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等
# def _private_1(name):
#     return 'Hello, %s' % name
#
# def _private_2(name):
#     return 'Hi, %s' % name
#
# def greeting(name):
#     if len(name) > 3:
#         return _private_1(name)
#     else:
#         return _private_2(name)
#我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，这样，调用greeting()函数不用关心内部的private函数细节