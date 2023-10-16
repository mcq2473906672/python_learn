# 计算密集型     进程√
# import time
# from multiprocessing import Process
# from threading import Thread
#
#
# def task():
#     res = 0
#     for i in range(180000000):
#         res += 1
#
#
# if __name__ == '__main__':
#     task_l = []
#     start = time.time()
#     for i in range(10):
#         # p = Process(target=task)    # 8s
#         p = Thread(target=task)  # 58s
#         p.start()
#         task_l.append(p)
#     for t in task_l:
#         t.join()
#     end = time.time() - start
#     print(f"花费时间：{end}")


# IO密集型     线程√
import time
from multiprocessing import Process
from threading import Thread


def task():
    time.sleep(1)


if __name__ == '__main__':
    start = time.time()
    task_l = []
    for i in range(4000):
        # t = Process(target=task)        # 46s
        t = Thread(target=task)         # 1.5s
        t.start()
        task_l.append(t)
    for t in task_l:
        t.join()
    end = time.time() - start
    print(f"花费时间：{end}")
