from threading import Thread, RLock
import time

num = 180


def task(mutex):
    global num
    # mutex.acquire()
    with mutex:
        temp = num
        time.sleep(0.1)
        num = temp - 1
    # mutex.release()


if __name__ == '__main__':
    l = []
    for i in range(180):
        t = Thread(target=task)
        t.start()
        l.append(t)
    for t in l:
        t.join()
    print(num)
