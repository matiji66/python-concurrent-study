#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# 实现了进程之间的数据共享 进程Manager：真正实现进程间的数据共享（不只是数据传递）

from multiprocessing import Process, Manager
import os


def f(d, l):
    d["name"] = "alex"
    d["sex"] = "Man"
    d["age"] = 33

    l.append(os.getpid())
    print(l)


if __name__ == "__main__":
    with Manager() as manager:
        d = manager.dict()  # 生成一个字典，可以在多个进程直接共享和传递
        l = manager.list(range(5))  # 生成一个列表，可以在多个进程直接共享和传递

        res = []
        for i in range(10):
            p = Process(target=f, args=(d, l))
            p.start()
            res.append(p)

        for j in res:  # 等待结果
            j.join()

        print(d)
        print(l)
