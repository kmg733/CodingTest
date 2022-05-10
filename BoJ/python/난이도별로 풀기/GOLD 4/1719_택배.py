# https://www.acmicpc.net/problem/1719
import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())

# 플로이드-와샬 풀이

# # 간선 경로에 대한 비용 저장
# graph = [[INF] * (n + 1) for _ in range(n + 1)]
# # 결과 값 저장할 리스트
# result = [[0] * (n + 1) for _ in range(n + 1)]

# # 간선 경로에 대한 비용 저장
# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a][b] = c
#     graph[b][a] = c
#     result[a][b] = b
#     result[b][a] = a

# # 중간에 거쳐가는 노드
# for k in range(1, n + 1):
#     # 시작 노드
#     for a in range(1, n + 1):
#         # 도착 노드
#         for b in range(1, n + 1):
#             if graph[a][b] > graph[a][k] + graph[k][b]:
#                 graph[a][b] = graph[a][k] + graph[k][b]
#                 result[a][b] = result[a][k]

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == j:
#             print('-', end = ' ')
#         else:
#             print(result[i][j], end = ' ')
#     print()
# ===================================
# 다익스트라 풀이

# 결과 값을 저장할 리스트
result = [[0] * n for i in range(n)]
# 간선 정보 추가
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

def dijkstra(start):
    distance = [INF] * (n + 1)
    heap = []
    heapq.heappush(heap, [0, start])
    distance[start] = 0

    while heap:
        cost, node = heapq.heappop(heap)

        # 같은 경로로 가는 길이지만 비용이 더 드는 경우 continue
        # ex:
        # 1 2 2 
        # 1 2 10
        if distance[node] < cost:
            continue
        
        for nextCost, nextNode in graph[node]:
            newCost = nextCost + cost
            if distance[nextNode] > newCost:
                distance[nextNode] = newCost
                # 최단 거리 경로를 찾을 때마다 스타트 노드를 이용해 그 다음 노드 저장
                # 1번 노드에서 6번 노드까지 가는 최단 경로는
                # 6번 노드에서 1번 노드까지 가는 최단 경로와 같음
                # nextNode에 도달하기 직전에 방문한건 node
                result[nextNode - 1][start - 1] = node
                heapq.heappush(heap, [newCost, nextNode])

# 다익스트라 알고리즘을 n번 실행
# for i in range(1, n + 1):
#     dijkstra(i)
dijkstra(1)

for i in range(n):
    for j in range(n):
        if i == j:
            print("-", end = " ")
        else:
            print(result[i][j], end = " ")
    print()