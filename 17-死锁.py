from threading import Thread, RLock, current_thread
import time

mutex1 = RLock()
mutex2 = RLock()


def task():
    mutex1.acquire()
    print(current_thread().name, "抢到锁1")
    mutex2.acquire()
    print(current_thread().name, "抢到锁2")
    mutex1.release()
    mutex2.release()

    mutex2.acquire()
    print(current_thread().name, "抢到锁2")
    time.sleep(1)
    mutex1.acquire()
    print(current_thread().name, "抢到锁1")
    mutex1.release()
    mutex2.release()


if __name__ == '__main__':
    for i in range(8):
        t = Thread(target=task)
        t.start()
