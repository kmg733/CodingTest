# https://www.acmicpc.net/problem/9663
import sys
input = sys.stdin.readline

# 깊이 우선 탐색
def dfs(n):
    # 마지막인지 확인
    if n == N:
        global count
        count += 1
    else:
        for i in range(N):
            if visited[i]:
                continue

            board[n] = i

            # 퀸이 안겹치는지 확인 
            if check(n):
                visited[i] = True
                dfs(n+1)
                visited[i] = False

# 퀸이 안겹치는지 확인
def check(n):
    for i in range(n):
        # 같은 열에 있거나 대각선 상에 있는지 확인
        if (board[n] == board[i]) or (n - i == abs(board[n] - board[i])):
            return False

    return True

N = int(input())
count = 0
# 복잡함과 시간초과 문제를 해결하기위해 1차원 리스트를 사용한다.
# 인덱스 == 행, 값 == 열
board = [0 for _ in range(N)]
visited = [False for _ in range(N)]

dfs(0)
print(count)