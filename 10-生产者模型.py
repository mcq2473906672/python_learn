from multiprocessing import Process, Queue, JoinableQueue
import time, random


def produecer(name, food, q):
    for i in range(4):
        time.sleep(2)
        print(f"{name}生产了{food}{i}")
        q.put(f"{food}{i}")


def consumer(name, q):
    while True:
        food = q.get()
        time.sleep(1)
        print(f"{name}吃了{food}")
        # if food == 'baba':
        #     break
        q.task_done()


if __name__ == '__main__':
    q = JoinableQueue()
    p1 = Process(target=produecer, args=('mcq', 'fish', q))
    p2 = Process(target=produecer, args=('avb', 'dsa', q))
    c1 = Process(target=consumer, args=('bajie', q))
    c2 = Process(target=consumer, args=('wukong', q))
    p1.start()
    p2.start()
    c1.daemon = True
    c2.daemon = True
    c1.start()
    c2.start()
    p1.join()
    p2.join()
    # q.put("baba")
    # q.put("baba")
    q.join()      # 等待队列中所有数据被取完 计数器变成0 往后执行代码
