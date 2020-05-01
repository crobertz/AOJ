# ALDS1_3_C
# Queue

import sys
from collections import deque

_, quantum = tuple(int(n) for n in input().split())

q = deque([(lambda x,y: [x, int(y)])(*tuple(line.strip().split())) \
        for line in sys.stdin.readlines()])

current_time = 0
task_end = deque()

while q:
    task_pair = q.popleft()
    if task_pair[1] <= quantum:
        current_time += task_pair[1]
        task_end.append([task_pair[0], current_time])
    else:
        task_pair[1] -= quantum
        q.append(task_pair)
        current_time += quantum

for pair in task_end:
    print('{} {}'.format(*pair))