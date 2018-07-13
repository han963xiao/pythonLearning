#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#上一个方法from multiprocessing import Process 只能够建立一个进程，现在这个可以建立很多个
#

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    #重复的给参数！！！args都是long_time_task这个函数的参数
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    #关闭pool不在创建进程了！
    p.close()
    #调用join之前，一定要先调用close() 函数，否则会出错, close()执行后不会有新的进程加入到pool,join函数等待所有子进程结束
    #由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果
    p.join()
    print('All subprocesses done.')
