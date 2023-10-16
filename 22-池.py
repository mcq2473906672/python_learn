from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
import os

# pool = ThreadPoolExecutor(10)     # 默认为cpu * 5
pool = ProcessPoolExecutor(3)  # 默认为cpu个数


def task(name):
    print(f"{name},{os.getpid()}")
    time.sleep(3)
    return name


def call_back(res):
    print(f"call_back{res.result()}")


if __name__ == '__main__':
    f_list = []
    for i in range(50):
        future = pool.submit(task, i).add_done_callback(call_back)
        f_list.append(future)

    # pool.shutdown()  # 等待任务运行完毕
    # for f in f_list:
    #     print(f"任务结果：{f.result()}")
    print("主线程")
