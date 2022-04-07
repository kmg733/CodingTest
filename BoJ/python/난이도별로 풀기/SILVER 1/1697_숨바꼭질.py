# https://www.acmicpc.net/problem/1697
from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
MAX = 10 ** 5
dist = [0] * (MAX + 1)

def bfs(start):
    que = deque()
    que.append(start)

    while(que):
        q = que.popleft()
        if q == k:
            print(dist[q])
            break
        for j in (q - 1, q + 1, q * 2):
            if j >= 0 and j <= MAX and dist[j] == 0:
                dist[j] = dist[q] + 1
                que.append(j)

bfs(n)

# DFS/BFS