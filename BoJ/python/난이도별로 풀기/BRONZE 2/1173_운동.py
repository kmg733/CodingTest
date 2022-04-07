# https://www.acmicpc.net/problem/1173
import sys

N, m, M, T, R = map(int, sys.stdin.readline().split())

X = m
exTime = 0
totalTime = 0
while True:
    if M - m < T:
        totalTime = -1
        break

    totalTime += 1
    if X + T > M:
        X -= R
        if X < m:
            X = m
    else:
        X += T
        exTime += 1
        if exTime == N:
            break

print(totalTime)