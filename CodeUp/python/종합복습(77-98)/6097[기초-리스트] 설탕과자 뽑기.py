import sys

h, w = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())

f = []
for i in range(h):
    f.append([])
    for j in range(w):
        f[i].append(0)

for i in range(n):
    l, d, x, y = map(int, sys.stdin.readline().split())

    if d == 0:
        for j in range(l):
            f[x-1][y-1+j] = 1
    else:
        for j in range(l):
            f[x-1+j][y-1] = 1

for i in range(h):
    for j in range(w):
        print(f[i][j], end=' ')
    print()