# https://www.acmicpc.net/problem/1167
from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v = int(input())
graph = [[] for _ in range(v + 1)]

for _ in range(v):
    n = list(map(int, input().split()))
    for e in range(1, len(n) - 2, 2):
        # 시작노드.append([노드, 비용])
        graph[n[0]].append([n[e], n[e + 1]])


# bfs 풀이
def bfs(start, mode):
    que = deque()
    que.append(start)
    costs = [-1] * (v + 1)
    costs[start] = 0
    
    while que:
        curNode = que.popleft()

        # 다음노드, 다음노드 간선의 비용
        for nextNode, nextCost in graph[curNode]:
            # 방문한 적이 없으면
            if costs[nextNode] == -1:
                costs[nextNode] = costs[curNode] + nextCost
                que.append(nextNode)
    
    # 처음 선택한 노드에서 가장 먼 노드 리턴
    if mode == 1:
        return costs.index(max(costs))
    # 두 번째 선택한 노드에서 가장 먼 노드와의 거리 리턴
    else:
        return max(costs)

print(bfs(bfs(1, 1), 2))

# dfs 풀이
def dfs(curNode):
    for nextNode, nextCost in graph[curNode]:
        if costs[nextNode] == -1:
            costs[nextNode] = costs[curNode] + nextCost
            dfs(nextNode)

costs = [-1] * (v + 1)    
costs[1] = 0
dfs(1)

t = costs.index(max(costs))
costs = [-1] * (v + 1)    
costs[t] = 0
dfs(t)
print(max(costs))