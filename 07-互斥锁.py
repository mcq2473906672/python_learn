from multiprocessing import Process, Lock
import time
import json
import random


# 查票
def search_ticket(name):
    with open('./data/tickes', 'r', encoding='utf-8') as f:
        dic = json.load(f)
        print(f'用户{name}查询余票：{dic.get("tickets_num")}]')


# 买票
def buy_ticket(name):
    with open('./data/tickes', 'r', encoding='utf-8') as f:
        dic = json.load(f)
    time.sleep(random.randint(1, 5))
    if dic.get("tickets_num") > 0:
        dic['tickets_num'] -= 1
        with open('./data/tickes', 'w', encoding='utf-8') as f:
            json.dump(dic, f)
        print(f"用户{name}买票成功")
    else:
        print(f"余票不足 用户{name}买票失败")


def task(name, lock):
    search_ticket(name)
    lock.acquire()
    buy_ticket(name)
    lock.release()


if __name__ == '__main__':
    mutax = Lock()
    for i in range(1, 9):
        p = Process(target=task, args=(i, mutax))
        p.start()
    print("123")
