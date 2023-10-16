# 方式一
from multiprocessing import Process
import time


def func(name, n):
    print(f"{name}")
    time.sleep(n)
    print(f'{name}任务结束')


if __name__ == '__main__':
    l = []
    for i in range(1, 4):
        p = Process(target=func, args=(f'mcq{i}', i))
        p.start()
        l.append(p)
    for p in l:
        p.join()
    print("主进程")
