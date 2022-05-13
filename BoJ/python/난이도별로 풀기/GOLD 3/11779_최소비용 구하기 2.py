# https://www.acmicpc.net/problem/11779
import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())
costs = [INF] * (n + 1)
# 부모 노드를 저장할 리스트
parent = [-1 for _ in range(n + 1)]

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append([c, e])

startNode, endNode = map(int, input().split())

# 다익스트라
def dijkstra(start):
    costs[start] = 0
    heap = []
    heapq.heappush(heap, [0, start])

    while heap:
        curCost, curNode = heapq.heappop(heap)

        # 기존 저장된 탐색 비용보다 현재 탐색 비용이 더 크다면
        if costs[curNode] < curCost:
            continue

        for nextCost, nextNode in graph[curNode]:
            sumCost = curCost + nextCost
            # 저장되어 있는 비용이 현재 비용보다 클 때 최단거리 갱신
            if costs[nextNode] > sumCost:
                costs[nextNode] = sumCost
                heapq.heappush(heap, [sumCost, nextNode])
                # 최단 거리가 갱신 되면 nextNode의 부모 노드인 curNode를 저장
                parent[nextNode] = curNode

dijkstra(startNode)
print(costs[endNode])

path = []
temp = endNode
while True:
    path.append(temp)
    if temp == startNode:
        break
    temp = parent[temp]

print(len(path))
path.reverse()
print(*path)