# 方式一
# from multiprocessing import Process
# import time
#
#
# def func(name):
#     print("1")
#     time.sleep(5)
#     print(f'{name}任务结束')
#
#
# if __name__ == '__main__':
#     # 1、得到进程操作对象
#     p = Process(target=func, args=('mcq',))
#     # 2、创建进程
#     p.start()
#     print("主进程")


# 方式2
from multiprocessing import Process
import time


class MyProcess(Process):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self) -> None:
        print(f"{self.name}任务开始")
        time.sleep(3)
        print(f"{self.name}任务结束")


if __name__ == '__main__':
    p = MyProcess("mcq")
    p.start()
    print("主进程")
