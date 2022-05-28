# https://www.acmicpc.net/problem/1939
from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

for i in range(1, n + 1):
    graph[i].sort(key=lambda x:-x[1])

start, end = map(int, input().split())

visited = [0] * (n + 1)
# bfs와 이분 탐색을 이용한 풀이
# bfs로 start에서 end로 갈 수 있는 경로 찾음
def bfs(cost):
    que = deque()
    que.append(start)
    visited[start] = 1

    while que:
        node = que.popleft()

        for nextNode, nextCost in graph[node]:
            # 방문한 적이 없고, 이전 중량보다 현재 다리의 중량이 크거나 같을 때
            if visited[nextNode] == 0 and nextCost >= cost:
                visited[nextNode] = 1
                que.append(nextNode)

minc, maxc = 1, 1000000000
while minc < maxc:
    mid = (maxc + minc) // 2

    if bfs(mid):