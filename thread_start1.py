#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import threading
import time

# 启线程法2（类）：


def func(name):
    print("hello", name)
    time.sleep(3)


t1 = threading.Thread(target=func, args=("alex",))
t2 = threading.Thread(target=func, args=("zingp",))

t1.start()  # 并发
t2.start()  # 并发
t1.join()
t2.join()

# func("alex")    # 先执行
# func("zingp")   # 再执行
