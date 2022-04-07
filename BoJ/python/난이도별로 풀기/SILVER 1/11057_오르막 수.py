# https://www.acmicpc.net/problem/11057
import sys
input = sys.stdin.readline

n = int(input())
# dp 테이블
d = [[0] * 10 for i in range(n + 1)]

for i in range(10):
    d[0][i] = 1

for i in range(1, n + 1):
    for j in range(10):
        for k in range(j + 1):
            d[i][j] += d[i - 1][k]

print(d[n][9] % 10007)

# 참고: https://kyoung-jnn.tistory.com/entry/%EB%B0%B1%EC%A4%8011057%EB%B2%88%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EC%98%A4%EB%A5%B4%EB%A7%89-%EC%88%98-DP
# DP