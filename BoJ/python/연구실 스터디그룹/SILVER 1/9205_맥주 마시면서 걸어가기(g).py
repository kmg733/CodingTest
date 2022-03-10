# https://www.acmicpc.net/problem/9205
from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

def bfs():
    que = deque()
    que.append((startX, startY))

    while que:
        x, y = que.popleft()
        # 목표 노드의 거리가 1000미터 내에 있는지 확인
        if abs(x - endX) + abs(y - endY) <= 1000:
            print("happy")
            return

        for i in range(n):
            if visited[i] == 0:
                newX, newY = conven[i]
                # 편의점을 확인하면서 1000미터 내에 있는지 확인
                # 있다면 해당 편의점을 큐에 추가
                if abs(x - newX) + abs(y - newY) <= 1000:
                    que.append((newX, newY))
                    visited[i] = 1
    
    print("sad")
    return

for _ in range(t):
    n = int(input())

    startX, startY = map(int, input().split())
    conven = []
    for _ in range(n):
        conven.append(list(map(int, input().split())))
    endX, endY = map(int, input().split())
    visited = [0 for i in range(n + 1)]    
    bfs()

# DFS/BFS