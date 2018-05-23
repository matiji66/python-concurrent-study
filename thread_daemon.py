#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import threading
import time

# 3.3 Daemon：设置守护线程。程序会等待【非守护线程】结束才退出，不会等【守护线程】


def func(name):
    print("i am ", name)
    time.sleep(1)
    print("this tread done...")


star_time = time.time()

# 这里主线程和主线  程启动的50个线程均为并行，互不影响；相当于51个线程并发

for i in range(50):
    t = threading.Thread(target=func, args=(i,))
    t.setDaemon(True)  # 将当前线程设置为守护线程，程序会等待【非守护线程】结束才退出，不会等【守护线程】。
    t.start()

print("all tread has finished...", threading.current_thread(), threading.active_count())

print("total time:", time.time() - star_time)
