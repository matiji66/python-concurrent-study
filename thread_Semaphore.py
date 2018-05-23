#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import threading
import time

# Semaphore(信号量)
# 互斥锁 同时只允许一个线程更改数据，而Semaphore是同时允许一定数量的线程更改数据 ，
# 比如厕所有3个坑，那最多只允许3个人上厕所，后面的人只能等里面有人出来了才能再进去。


def func(n):
    semaphore.acquire()
    time.sleep(1)
    print("this thread is %s\n" % n)
    semaphore.release()


semaphore = threading.BoundedSemaphore(5)  # 信号量

for i in range(23):
    t = threading.Thread(target=func, args=(i,))
    t.start()

while threading.active_count() != 1:
    pass
    # print(threading.active_count())
else:
    print("all threads is done...")
