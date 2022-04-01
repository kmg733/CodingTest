# https://www.acmicpc.net/problem/1967
from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# - 트리의 지름 풀이 -
# 한 노드를 선택해서 그 노드로부터 가장 먼 노드 t를 구하고,
# t에서부터 가장 먼 노드 u를 구한 뒤,
# t와 u사이의 거리를 구하면 트리의 지름이 나온다.(귀류법)

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    fromNode, toNode, cost = map(int, input().split())
    # 무방향 그래프 이므로 부모와 자식노드를 서로 연결
    graph[fromNode].append([toNode, cost])
    graph[toNode].append([fromNode, cost])

# bfs 풀이
def bfs(startNode, mode):
    que = deque()
    que.append(startNode)
    costs = [-1 for _ in range(n + 1)]
    costs[startNode] = 0

    while que:
        curNode = que.popleft()
        for nextNode, cost in graph[curNode]:
            if costs[nextNode] == -1:
                # 다음 노드까지의 비용 = 현재 노드까지의 비용 + 다음 노드를 가는데 드는 비용
                costs[nextNode] = costs[curNode] + cost
                que.append(nextNode)
    
    
    if mode == 1:
        return costs.index(max(costs)) 
    else:
        return max(costs)

print(bfs(bfs(1, 1), 2))

# dfs 풀이
# 시작 노드로부터의 거리 비용을 구해서 costs에 저장
def dfs(curNode, curCost):
    for nextNode, nextCost in graph[curNode]:
        if costs[nextNode] == -1:
            costs[nextNode] = nextCost + curCost
            dfs(nextNode, costs[nextNode])

costs = [-1 for _ in range(n + 1)]
costs[1] = 0
dfs(1, 0)
# costs에서 가장 큰값의 index값이 1번 노드로부터 가장 멀리있는 t노드임
t = costs.index(max(costs))
# t노드로부터의 거리를 costs에 저장하고, 가장 큰 max값이 u노드와의 거리이므로 이를 출력하면 끝
costs = [-1 for _ in range(n + 1)]
costs[t] = 0
dfs(t, 0)
print(max(costs))

# 참고 
# bfs 풀이 : https://chldkato.tistory.com/29
# dfs 풀이 : https://kyun2da.github.io/2021/05/04/tree's_diameter/
