# https://www.acmicpc.net/problem/1504
import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

n, e = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for i in range(e):
    a, b, v = map(int, input().split())
    graph[a].append([v, b])
    graph[b].append([v, a])

# 반드시 거쳐야 하는 두 개의 서로 다른 정점
# v1과 v2 정점을 반드시 거쳐야 함
v1, v2 = map(int, input().split())

def dijkstra(startNode):
    distance = [INF for _ in range(n + 1)]
    # 시작지점 비용 0
    distance[startNode] = 0
    heap = []
    # 우선순위 큐 사용으로, 더 적은 비용이 드는 간선을 우선 탐색
    heapq.heappush(heap, [0, startNode])    

    while heap:
        cost, node = heapq.heappop(heap)

        # 현재 저장되어 있는 비용보다 현재 탐색하는 비용이 더 크면 continue
        if distance[node] < cost:
            continue
        
        for nextCost, nextNode in graph[node]:
            newCost = nextCost + cost
            # 다음 노드의 기존 비용이 현재 탐색한 비용보다 더 크면
            if distance[nextNode] > newCost:
                # 비용이 더 적게 드는 값으로 대체
                distance[nextNode] = newCost
                # 해당 노드 탐색
                heapq.heappush(heap, [newCost, nextNode])
    return distance

# 시작 지점 1을 기준으로 각 노드까지 최소 비용
d1 = dijkstra(1)
# 시작 지점 v1를 기준으로 각 노드까지 최소 비용
d2 = dijkstra(v1)
# 시작 지점 v2를 기준으로 각 노드까지 최소 비용
d3 = dijkstra(v2)
result = min(d1[v1] + d2[v2] + d3[n], d1[v2] + d3[v1] + d2[n])
if result < INF:
    print(result)
else:
    print(-1)