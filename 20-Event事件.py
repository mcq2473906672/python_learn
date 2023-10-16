from threading import Thread, Event
import time

event = Event()


def bus():
    print("公车快到了")
    time.sleep(3)
    print("公车到了")
    event.set()


def passenger(name):
    print(f"{name}正在等车")
    event.wait()
    print(f"{name}上车出发")


if __name__ == '__main__':
    t = Thread(target=bus)
    t.start()

    for i in range(10):
        t = Thread(target=passenger, args=(f"乘客{i}",))
        t.start()