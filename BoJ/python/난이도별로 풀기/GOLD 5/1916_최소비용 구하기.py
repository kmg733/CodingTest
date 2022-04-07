# https://www.acmicpc.net/problem/1916
import sys
import heapq
INF = sys.maxsize
input = sys.stdin.readline

# startNode부터 모든 노드까지의 최소 비용 계산해서 dist에 저장 
def dijkstra(startCost, startNode):
    # startNode 부터 n번 노드까지 가는데 드는 비용을 저장 할 리스트 
    # 최소 비용을 구하는 것이므로 dist 리스트에 최대값을 저장
    dist = [INF for _ in range(n + 1)]

    # 시작 노드의 비용은 0
    dist[startNode] = 0
    # 시작 비용과 노드를 우선순위 큐에 넣어 줌
    q = [(startCost, startNode)]

    # 연결된 노드가 있는 동안
    while q:
        # 우선순위 큐에 들어있는 노드 중 비용이 가장 적은걸 가져옴
        p = heapq.heappop(q)
        curCost, curNode = p[0], p[1]
        
        # 같은 경로로 가는 길이지만 비용이 더 드는 경우 continue <- 이게 있어야 시간초과 안남
        # ex:
        # 1 2 2 
        # 1 2 10
        if dist[curNode] < curCost:
            continue
        
        # 현재 노드와 연결된 노드들 까지 가는데 드는 비용 계산
        for nextCost, nextNode in graph[curNode]:
            # 기존에 저장된 노드 비용 > 현재까지 거쳐오면서 든 비용 + 다음 노드까지 가는데 드는 비용
            if dist[nextNode] > curCost + nextCost:
                # 비용이 더 적은 값 저장
                dist[nextNode] = curCost + nextCost
                
                # 다음 노드를 우선순위 큐에 추가
                heapq.heappush(q, (dist[nextNode], nextNode))

    return dist

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    start, end, cost = map(int, input().split())
    # start 노드에 연결된 end node들과 비용을 추가
    graph[start].append((cost, end))

startT, targetT = map(int, input().split())
print(dijkstra(0, startT)[targetT])

# 다익스트라
# 참고: https://velog.io/@uoayop/BOJ-1916-%EC%B5%9C%EC%86%8C-%EB%B9%84%EC%9A%A9-%EA%B5%AC%ED%95%98%EA%B8%B0Python