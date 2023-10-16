from multiprocessing import Process, current_process
import os, time


def task():
    # print(f"任务{current_process().pid}执行中")
    print(f"任务{os.getpid()}执行中")


if __name__ == '__main__':
    p = Process(target=task)
    p.start()
    print("主进程",current_process().pid)
