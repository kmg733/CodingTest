# https://www.acmicpc.net/problem/1753
import sys, heapq
input = sys.stdin.readline

# 정점의 갯수 v, 간선의 갯수 e
v, e = map(int, input().split())

# 시작 노드
s = int(input())

INF = sys.maxsize
# 초기 비용을 최대값으로 초기화
costs = [INF for _ in range(v + 1)]
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    f, t, w = map(int, input().split())
    graph[f].append([w, t])

# 최단경로는 다익스트라(우선순위 큐) 써서 풀기
def dijkstra():
    heap = []
    heapq.heappush(heap, (0, s))
    costs[s] = 0

    while heap:
        nowWeigh, nowNode = heapq.heappop(heap)

        if costs[nowNode] < nowWeigh:
            continue
        
        # 연결된 노드들 비용 확인
        for nextWeigh, nextNode in graph[nowNode]:
            # 현재 계산한 비용이 기존 비용보다 적다면
            if costs[nextNode] > nextWeigh + nowWeigh:
                costs[nextNode] = nextWeigh + nowWeigh
                heapq.heappush(heap, (costs[nextNode], nextNode))

dijkstra()
for i in range(1, v + 1):
    if costs[i] == INF:
        print("INF")
    else:
        print(costs[i])