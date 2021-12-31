# https://www.acmicpc.net/problem/1388
import sys

n, m = map(int, sys.stdin.readline().split())

plate = []
for _ in range(n):
    plate.append(list(sys.stdin.readline()))

count = 0
for i in range(n):
    chk = '?'
    for j in range(m):
        if plate[i][j] != chk:
            if plate[i][j] == '-':
                chk = '-'
                count += 1
            else:
                chk = '|'

for i in range(m):
    chk = '?'
    for j in range(n):
        if plate[j][i] != chk:
            if plate[j][i] == '-':
                chk = '-'
            else:
                chk = '|'
                count += 1

print(count)