# https://www.acmicpc.net/problem/1913
import sys
input = sys.stdin.readline

# 달팽이 표 만들기
def makeSnail(n):
    
    snail = [[0 for _ in range(n)] for _ in range(n)]

    x = 0   # 행
    y = 0   # 열
    d = 0   
    nowNum = n**2
    # 바깥에서부터 아래 오른쪽 위쪽 왼쪽 순서로 번호가 찍힘
    move = [[1, 0], [0, 1], [-1, 0], [0, -1]] 

    # 숫자 넣기
    while nowNum > 0:
        snail[x][y] = nowNum
        # 표를 넘어가는지 체크
        if x + move[d][0] < 0 or x + move[d][0] >= n or y + move[d][1] < 0 or y + move[d][1] >= n or snail[x + move[d][0]][y + move[d][1]] != 0:
            d = (d + 1) % 4
        x += move[d][0]
        y += move[d][1]
        nowNum -= 1

    return snail


# 시작지점은 (N - 1) / 2
n = int(input())
f = int(input())

snail = makeSnail(n)

# 원하는 숫자 찾기
for i in range(n):
    for j in range(n):
        if snail[i][j] == f:
            x, y = i + 1, j + 1
        print(snail[i][j], end=' ')
    print()
print(x, y)