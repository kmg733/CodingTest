# https://www.acmicpc.net/problem/12886
import sys
from collections import deque

input = sys.stdin.readline
a, b, c = map(int, input().split())

# 문제의 조건에서 같은 x값을 더하고 빼기 때문에
# a, b, c를 합친 total 값은 항상 똑같다는 규칙이 있음
total = sum([a, b, c])

# 이부분 때문에 시간이 너무 오래걸림
# # visited 크기를 알 수 없으므로 defaultdict 선언
# # visited = defaultdict(int)

# 시간 때문에 개선한 부분
# - 각 돌이 가질 수 있는 최대값은 total임 때문에 크기가 total + 1인 리스트 생성
# - 원래는 a, b, c값에 대해서 3차원 리스트를 만들어야 하지만 c값은 a, b값으로 알수 있으므로 2차원 리스트로 생성
visited = [[0] * (total + 1) for _ in range(total + 1)]

def bfs(a, b, c):
    que = deque()
    que.append([a, b])
    visited[a][b] = 1
    
    while que:
        x, y = que.popleft()
        z = total - (x + y)
        if x == y == z:
            return 1
        
        for a, b in (x, y), (y, z), (x, z):
            if a < b:
                b -= a
                a += a
            elif a > b:
                a -= b
                b += b
            # 값이 같은경우는 건너뛰기
            else:
                continue

            c = total - (a + b)
            # 중복 탐색 제거를 위한 x, y값 설정
            x = min(a, b, c)
            y = max(a, b, c)
            if visited[x][y] == 0:
                visited[x][y] = 1
                que.append([x, y])

    # 데크 안의 리턴문이 안걸리면 a, b, c를 같게 만들 수 없다는 뜻이므로 0리턴
    return 0

# 메모리 초과나서 찾아본 결과 총 돌의 개수가 3의 배수가 아니면
# a, b, c를 같게 만들 수 없다는 규칙이 있음
if total % 3 != 0:
    print(0)
else:
    print(bfs(a, b, c))
