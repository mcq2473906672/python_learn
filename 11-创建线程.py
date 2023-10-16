from multiprocessing import Process
from threading import Thread
import time


def task(name):
    print(f"{name} 任务开始")
    time.sleep(3)
    print(f"{name} 任务结束")


# if __name__ == '__main__':
t = Thread(target=task, args=("mcq",))
t.start()
print("主线程")
