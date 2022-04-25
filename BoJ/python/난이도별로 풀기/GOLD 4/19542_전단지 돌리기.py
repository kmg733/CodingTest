# https://www.acmicpc.net/problem/19542
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(curNode, preNode):
    # answer는 방문한 노드의 개수
    global answer
    # maxD는 리프 노드로부터 현재 노드까지의 거리
    maxD = 0
    for nextNode in graph[curNode]:
        # 양방향으로 연결된 간선이기 때문에
        # 다음에 방문할 노드가 전에 방문한 노드인지 확인
        if nextNode != preNode:
            maxD = max(maxD, dfs(nextNode, curNode))

    # 리프 노드에서부터 현재 노드까지의 거리(maxD)가 d보다 크거나 같다면 이동거리 1씩 증가
    if maxD >= d:
        answer += 1

    return maxD + 1

n, s, d = map(int, input().split())
graph = [[] for i in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = 0
dfs(s, 0)
if answer:
    print(2 * (answer - 1))
else:
    print(0)