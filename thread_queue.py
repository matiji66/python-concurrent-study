#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# 正常的队列是先进先出 Queue.join() block直到queue被消费完毕
import queue

q = queue.Queue(maxsize=10)  # 设置队列大小，默认为无限大

q.put(1)
q.put(8)
q.put("alex")
q.put("zingp")

print(q.get())
print(q.get())
print(q.get())
print(q.get())

# 1
# 8
# alex
# zingp
# print(q.get(timeout=5))
# put()和get()都可以设置超时时间，若设置，超时会报错。没设置则会卡住（阻塞）

q2 = queue.LifoQueue()  # 后进先出
q2.put(1)
q2.put(2)
q2.put("zingp")

print(q2.get())
print(q2.get())
print(q2.get())
# zingp
# 2
# 1

q3 = queue.PriorityQueue()  # 设置优先级

q3.put((-1, "chenronghua"))
q3.put((6, "hanyang"))
q3.put((10, "alex"))
q3.put((4, "wangsen"))

print(q3.get())
print(q3.get())
print(q3.get())
print(q3.get())

# (-1, 'chenronghua')
# (4, 'wangsen')
# (6, 'hanyang')
# (10, 'alex')
