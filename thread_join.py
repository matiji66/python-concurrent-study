#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import threading
import time

# 3.2. join()：主程序（主线程）会等待其他线程执行完


def func(name):
    print("i am ", name)
    time.sleep(3)
    print("this tread done...")


if __name__ == '__main__':

    star_time = time.time()

    # 这里主线程和主线程启动的50个线程均为并行，互不影响；相当于51个线程并发
    res = []
    for i in range(50):
        t = threading.Thread(target=func, args=(i,))
        t.start()
        res.append(t)  # 每启动一个线程，就将这个实例加入列表

    for j in res:  # 历遍所启动的50个线程实例
        j.join()

    print("all tread has finished...", threading.current_thread())

    print("total time:", time.time() - star_time)
