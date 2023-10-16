from multiprocessing import Process
import time


def task(name):
    print(name, '还活着')
    time.sleep(3)
    print(name, "正常死亡")


if __name__ == '__main__':
    p = Process(target=task, args=('mcq',))
    p.daemon = True
    p.start()
    time.sleep(4)
    print("主程序")
