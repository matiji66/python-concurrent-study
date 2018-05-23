#! /usr/bin/env python3
# -*- coding:utf-8 -*-


import threading
import time

# 3.1启线程法1：
# tread类方法调用


class MyTread(threading.Thread):
    def __init__(self, name):
        super(MyTread, self).__init__()
        self.name = name

    def run(self):
        print("hello", self.name)
        time.sleep(3)


t1 = MyTread("alex")
t2 = MyTread("zingp")

t1.start()  # 并发
t2.start()  # 并发
