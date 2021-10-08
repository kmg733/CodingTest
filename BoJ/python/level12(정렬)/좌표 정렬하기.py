import sys

n = int(input())

xy = []

for _ in range(n):
    xy.append(list(map(int, sys.stdin.readline().split())))

xy.sort()
for a, b in xy:
    print(a, b)

# 2차원 리스트 정렬 참고: https://asxpyn.tistory.com/75