# from threading import Thread
# import time
#
#
# def task(name):
#     print(f"{name} 还活着")
#     time.sleep(3)
#     print(f"{name} 死亡")
#
#
# if __name__ == '__main__':
#     t = Thread(target=task, args=("mcq",))
#     t.daemon = True
#     t.start()
#     print("主线程")

# 案例：
from threading import Thread
import time


def f1():
    print("任务1开始")
    time.sleep(1)
    print("任务1结束")


def f2():
    print("任务2开始")
    time.sleep(1)
    print("任务2结束")


if __name__ == '__main__':
    t1 = Thread(target=f1)
    t2 = Thread(target=f2)
    t1.daemon = True

    t1.start()
    t2.start()
    print("主线程")