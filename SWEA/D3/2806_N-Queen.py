# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV7GKs06AU0DFAXB&categoryId=AV7GKs06AU0DFAXB&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=30&pageIndex=2

t = int(input())

# 백 트래킹 - N-Queen이 가능한지 확인
def isNQueen(i):
    for j in range(i):
        # 같은 열인지 or 대각선에 겹치는지 확인
        if row[i] == row[j] or abs(row[i] - row[j]) == abs(i - j):
            return False

    return True

def dfs(i):
    global answer
    if i == n:
        answer += 1
        return
    
    else:
        for j in range(n):
            # i행 j열에 퀸을 놓음
            row[i] = j
            if isNQueen(i):
                dfs(i + 1)

for case in range(1, t + 1):
    n = int(input())
    answer = 0
    row = [0] * n

    dfs(0)
    print(f"#{case} {answer}")