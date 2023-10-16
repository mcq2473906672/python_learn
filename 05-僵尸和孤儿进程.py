from multiprocessing import Process
import time


def task():
    print("任务开始")
    time.sleep(5)
    print("任命结束")


if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    print("主进程")
