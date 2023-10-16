from multiprocessing import Queue

q = Queue(6)
q.put_nowait(1)
q.put_nowait(2)
q.put_nowait(3)
q.put_nowait(4)
q.put_nowait(5)
q.put_nowait(6)
print(q.full())
print(q.empty())
# 先进先出
v1 = q.get()
v2 = q.get()
print(v1)
print(v2)