# https://www.acmicpc.net/problem/14248
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
ai = list(map(int, input().split()))
s = int(input())

visited = [0] * n

def bfs(start):
    que = deque()
    que.append(start)
    visited[start] = 1
    result = 1

    while que:
        node = que.popleft()
        # 왼쪽 오른쪽 한번씩
        for i in [-ai[node], ai[node]]:
            d = node + i
            if 0 <= d < n and visited[d] == 0:
                que.append(d)
                visited[d] = 1
                result += 1
    return result

print(bfs(s-1))
