#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import threading
import time

# 通过Event来实现两个或多个线程间的交互，下面是一个红绿灯的例子，即起动一个线程做交通指挥灯，生成几个线程做车辆，车辆行驶按红灯停，绿灯行的规则。


def lighter():
    count = 0
    event.set()
    while True:
        if 5 < count < 10:
            event.clear()
            print("This is RED....")
        elif count > 10:
            event.set()
            count = 0
        else:
            print("This is GREEN...")
        time.sleep(1)
        count += 1


def car(name):
    while True:
        if event.is_set():
            print(" Green, The %s running...." % name)
            time.sleep(1)
        else:
            print("RED, the %s is waiting..." % name)
            event.wait()
            print("green, %s start going..." % name)


event = threading.Event()
light = threading.Thread(target=lighter, )
light.start()
car1 = threading.Thread(target=car, args=("Tesla",))
car1.start()
