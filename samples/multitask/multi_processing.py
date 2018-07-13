#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块
#从multiprocessing模块提供了一个Process类，导入这个类

from multiprocessing import Process
# 这里也导入了os模块
import os

# 子进程要执行的代码
#python中的多进程要比多线程好的多！
#这样就创立了一个进程
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

#if __name__ == '__main__' 就相当于是 Python 模拟的程序入口。Python 本身并没有规定这么写，这只是一种编码习惯。
# 由于模块之间相互引用，不同模块可能都有这样的定义
# 而入口程序只能有一个。到底哪个入口程序被选中，这取决于 __name__ 的值

#__name__ 是内置变量，用于表示当前模块的名字，同时还能反映一个包的结构
#如果我们执行这个py文件的话，这个是成立的，我们直接执行的就是下面的一段话
#但是这个py文件当做包导进去的时候下面这个是不执行的

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
   #target就是这个线程想要执行的目标函数，要注意args是一个tuple

    #p就是产生的这个进程,这里的args不是name是 他的那个函数run_proc所需要的参数就是test，args函数需要的参数
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
