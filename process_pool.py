#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# https://www.cnblogs.com/zingp/p/5878330.html
from multiprocessing import Pool
import os, time


# 进程池内部维护一个进程序列，当使用时，则去进程池中获取一个进程，如果进程池序列中没有可供使用的进进程，那么程序就会等待，直到进程池中有可用进程为止。
# 进程池中有两个方法：
#     apply
#     apply_async


def Foo(i):
    time.sleep(2)
    print("in process", os.getpid())
    return i + 100


def Bar(arg):
    print("-->exec done:", arg, os.getpid())


if __name__ == "__main__":
    pool = Pool(processes=3)  # 允许进程池同时放入5个进程
    print("主进程：", os.getpid())
    for i in range(10):
        pool.apply_async(func=Foo, args=(1,), callback=Bar)  # callback = 回调
        # 这里回调的函数是主进程去回调的（生产中若所有进程完毕后将结果写入数据库，只需要写个回调就行了，不必每个进程中写入数据库）
        # pool.apply(func=Foo,args=(1,))         # 串行
        # pool.apply_async(func=Foo,args=(1,))   # 并行

    print("end")
    pool.close()
    pool.join()  # 这里一定是先close再join否则会出问题。。。如果注释掉该句，程序会直接关闭
