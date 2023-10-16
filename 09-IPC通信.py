from multiprocessing import Process, Queue, current_process


def task1(q):
    q.put("123")


def task2(q):
    print(q.get())


if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=task1, args=(q,))
    p2 = Process(target=task2, args=(q,))
    p1.start()
    p2.start()
