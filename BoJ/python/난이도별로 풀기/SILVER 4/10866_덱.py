# https://www.acmicpc.net/problem/10866
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
que = deque()
for _ in range(n):
    a = input().split()
    if a[0] == "push_front":
        que.appendleft(a[1])
    elif a[0] == "push_back":
        que.append(a[1])
    elif a[0] == "pop_front":
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif a[0] == "pop_back":
        if que:
            print(que.pop())
        else:
            print(-1)
    elif a[0] == "size":
        print(len(que))
    elif a[0] == "empty":
        if len(que) == 0:
            print(1)
        else:
            print(0) 
    elif a[0] == "front":
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif a[0] == "back":
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])

