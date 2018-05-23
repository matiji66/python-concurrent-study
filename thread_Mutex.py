import time
import threading


# 3.4 线程锁、互斥锁Mutex
# 一个进程下可以启动多个线程，多个线程共享父进程的内存空间，也就意味着每个线程可以访问同一份数据，此时，如果2个线程同时要修改同一份数据，会出现什么状况？

def addNum():
    global num  # 在每个线程中都获取这个全局变量
    print('--get num:', num)
    time.sleep(1)
    num -= 1  # 对此公共变量进行-1操作


num = 100  # 设定一个共享变量
thread_list = []
for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)

for t in thread_list:  # 等待所有线程执行完毕
    t.join()

print('final num:', num)