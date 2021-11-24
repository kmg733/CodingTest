import sys

n = int(input())

xy = []

for _ in range(n):
    xy.append(list(map(int, sys.stdin.readline().split())))

xy.sort(key=lambda x:(x[1], x[0]))
for a, b in xy:
    print(a, b)

# 2차원 리스트 정렬 참고: https://asxpyn.tistory.com/75