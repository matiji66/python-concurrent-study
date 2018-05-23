from multiprocessing import Process, Lock

# 进程同步 Without using the lock output from the different processes is liable to get all mixed up.


def f(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()


if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()
