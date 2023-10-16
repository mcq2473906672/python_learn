# import time
#
#
# # 计算密集型
# # 串行执行 0.67s
# def f1():
#     n = 0
#     for i in range(10000000):
#         n += i
#
#
# def f2():
#     n = 0
#     for i in range(10000000):
#         n += i
#
#
# if __name__ == '__main__':
#     start = time.time()
#     f1()
#     f2()
#     end = time.time() - start
#     print(end)

# import time
#
#
# # 计算密集型
# # 协程 1s
# def f1():
#     n = 0
#     for i in range(10000000):
#         n += i
#         yield
#
#
# def f2():
#     g = f1()
#     n = 0
#     for i in range(10000000):
#         n += i
#         next(g)
#
#
# if __name__ == '__main__':
#     start = time.time()
#     f2()
#     end = time.time() - start
#     print(end)


# IO密集型
from gevent import monkey

monkey.patch_all()
from gevent import spawn
import time


def da():
    for _ in range(3):
        print("A")
        time.sleep(2)


def mie():
    for _ in range(3):
        print("B")
        time.sleep(2)


def ccc():
    for _ in range(3):
        print("C")
        time.sleep(3)


if __name__ == '__main__':
    start = time.time()
    g1 = spawn(da)
    g2 = spawn(mie)
    g3 = spawn(ccc)
    g1.join()
    g2.join()
    g3.join()
    end = time.time() - start
    print(end)  # 单线程12s    协程6s
