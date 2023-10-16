import random
from threading import Thread, Semaphore
import time

sp = Semaphore(5)


def task(name):
    sp.acquire()
    print(f"{name}抢到车位")
    time.sleep(random.randint(1, 3))
    sp.release()


if __name__ == '__main__':
    for i in range(25):
        t = Thread(target=task, args=(f"车辆{i}号",))
        t.start()
