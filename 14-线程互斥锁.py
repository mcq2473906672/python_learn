from threading import Thread, RLock
import time

num = 100


def task(mutex):
    global num
    mutex.acquire()
    temp = num
    time.sleep(0.05)
    num = temp - 1
    mutex.release()


if __name__ == '__main__':
    l = []
    q = RLock()
    for i in range(100):
        t = Thread(target=task, args=(q,))
        t.start()
        l.append(t)
    for t in l:
        t.join()
    print(num)
