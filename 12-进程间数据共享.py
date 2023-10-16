import time
from threading import Thread, current_thread, active_count
import os

age = 18


def task():
    global age
    age = 16
    print("子线程", os.getpid())
    print(current_thread().name)


if __name__ == '__main__':
    t = Thread(target=task)
    t2 = Thread(target=task)
    t.start()
    t2.start()
    t.join()
    print("主线程", os.getpid())
    print(age)
    print(current_thread().name)
    print("活跃的线程数量", active_count())
