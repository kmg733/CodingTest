# https://www.acmicpc.net/problem/1260
import sys
from collections import deque

input = sys.stdin.readline

# 깊이 우선 탐색
def dfs(start, visited=[]):
    visited.append(start)
    print(start, end=' ')

    # 깊이 우선 탐색은 값 하나를 찾으면 dfs를 호출하여 재귀적으로 문제를 해결
    for i in range(1, len(g[start])):
        if g[start][i] == 1 and (i not in visited):
            dfs(i, visited)

# 너비 우선 탐색
def bfs(start):
    visited = [start]
    # list의 pop은 O(N)의 시간복잡도를 가졌다.
    # 때문에 시간복잡도 O(1)인 deque를 사용한다.
    que = deque()
    que.append(start)

    while que:
        v = que.popleft()
        print(v, end=' ')

        # 너비 우선 탐색은 해당 행에 있는 값을 모두 찾고
        # 해당 값을 사용한 적이 없다면 deque에 저장
        # deque에 값이 존재한다면 하나씩 꺼내서 for문 실행
        for i in range(1, len(g[start])):
            if g[v][i] == 1 and (i not in visited):
                visited.append(i)
                que.append(i)

n, m, v = map(int, input().split())

# 편의를 위해 n*n 이 아니라 (n+1)*(n+1) 행렬 생성
# 0번 인덱스는 항상 0
g = [[0] * (n + 1) for _ in range(n + 1)]

# 노드
for _ in range(m):
    m1, m2 = map(int, input().split())
    # 노드간 양방향 연결
    g[m1][m2] = g[m2][m1] = 1

dfs(v)
print()
bfs(v)
