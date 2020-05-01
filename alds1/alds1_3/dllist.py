# ALDS1_3_D
# Doubly linked list

from collections import deque

q = deque()

N = int(input())
for _ in range(N):
    com = input()
    if com == 'deleteFirst':
        q.popleft()
    elif com == 'deleteLast':
        q.pop()
    else:
        com, key = com.split()
        if com == 'insert':
            q.appendleft(key)
        else:
            if key in q:
                q.remove(key)

print(' '.join(list(q)))