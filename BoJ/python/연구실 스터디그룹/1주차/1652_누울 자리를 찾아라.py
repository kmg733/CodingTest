# https://www.acmicpc.net/problem/1652
import sys

n = int(sys.stdin.readline())

f = []
for i in range(n):
    f.append(sys.stdin.readline().strip())

cnt = [0, 0]
for i in range(n):
    rowCnt = 0
    for j in range(n):
        if f[i][j] == '.':
            rowCnt += 1
        else:
            if rowCnt >= 2:
                cnt[0] += 1
            rowCnt = 0

        if j == n-1:
            if rowCnt >= 2:
                cnt[0] += 1

    colCnt = 0
    for j in range(n):
        if f[j][i] == '.':
            colCnt += 1
        else:
            if colCnt >= 2:
                cnt[1] += 1
            colCnt = 0

        if j == n-1:
            if colCnt >= 2:
                cnt[1] += 1
print(cnt[0]. cnt[1])