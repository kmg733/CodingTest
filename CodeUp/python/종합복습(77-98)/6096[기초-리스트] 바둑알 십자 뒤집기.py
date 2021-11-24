import sys

d = []
for i in range(19):
    d.append(list(map(int, sys.stdin.readline().split())))

n = int(sys.stdin.readline())

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    for j in range(19):
        if d[x-1][j] == 0:
            d[x-1][j] = 1
        elif d[x-1][j] == 1:
            d[x-1][j] = 0

        if d[j][y-1] == 0:
            d[j][y-1] = 1
        elif d[j][y-1] == 1:
            d[j][y-1] = 0

for i in range(len(d)):
    for j in range(len(d[0])):
        print(d[i][j], end=' ')
    print()