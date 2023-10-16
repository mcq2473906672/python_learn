import queue

# 后进先出
# q = queue.LifoQueue()
# q.put('a')
# q.put('b')
#
# print(q.get())


# 优先级
q = queue.PriorityQueue()
q.put((0, 'a'))
q.put((1, 'b'))
q.put((-2, 'c'))
print(q.get()[1])
