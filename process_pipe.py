#! /usr/bin/env python3
# -*- coding:utf-8 -*-
# 进程之间也可以通过管道通讯 4.4进程Pipe:通过管道实现进程间的通讯

from multiprocessing import Process, Pipe


def f(conn):
    conn.send([42, None, "hello from child"])  # 发数据
    conn.send([42, None, "hello from child"])  # 多次发数据
    print("from parent:", conn.recv())  # 收数据
    conn.close()


if __name__ == "__main__":
    parent_conn, child_conn = Pipe()  # 创建管道，通过管道实现进程间通讯
    p = Process(target=f, args=(child_conn,))
    p.start()
    print('------start------')
    print('recv ', parent_conn.recv())  # 接收数据
    print('recv ', parent_conn.recv())  # 多次接收数据

    parent_conn.send("hello zing......")
    p.join()
