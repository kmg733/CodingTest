# https://www.acmicpc.net/problem/5014
from collections import deque
import sys
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
button = [0] * (f + 1)

def bfs(start):
    que = deque()
    que.append(start)

    while que:
        q = que.popleft()
        if q == g:
            return button[g]
        for x in (q + u, q - d):
            if 0 < x <= f and x != s and button[x] == 0:
                button[x] = button[q] + 1
                que.append(x)

    if button[g] == 0:
        return 'use the stairs'
print(bfs(s))

# 다른 사람의 풀이
# import sys
# from collections import deque

# def bfs(v):
#     q = deque([v])
#     visited[v] = 1
#     while q:
#         v = q.popleft()
#         if v == G:
#             return count[G]
#         for i in (v+U, v-D): #U만큼 위로 or D만큼 아래로
#             if 0 < i <= F and not visited[i]:
#                 visited[i] = 1
#                 count[i] = count[v] + 1
#                 q.append(i)
#     if count[G] == 0:
#         return "use the stairs"

# input = sys.stdin.readline
# F, S, G, U, D = map(int, input().split())
# visited = [0 for i in range(F+1)]
# count = [0 for i in range(F+1)]
# print(bfs(S))

# DFS/BFS