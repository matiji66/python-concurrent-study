#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import multiprocessing
import os
import time
import threading


# 实现启十个进程，每个进程又启一个线程~~~


def thread_id():
    """获得线程ID。"""
    print(" thread..")
    print("thread_id：%s\n" % threading.get_ident())


def hello(name):
    time.sleep(2)
    print("hello %s..." % name)
    # 启一个线程
    t = threading.Thread(target=thread_id, )
    t.start()


def info(title):
    print(title)
    print("module name:", __name__)
    print("parent process:", os.getppid())
    print("process id:", os.getpid())
    print("\n")


def f(name):
    info("child process..")
    print("hello", name)


if __name__ == "__main__":  # windows环境下必须写这句，不写会报错
    info("\033[31;1m main process\033[0m ")
    p = multiprocessing.Process(target=f, args=("jack",))
    p.start()

    for i in range(10):
        # 启一个进程和一个线程的语法都差不多
        p = multiprocessing.Process(target=hello, args=("progress %s" % i,))
        p.start()
