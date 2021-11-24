import sys

n = int(sys.stdin.readline())

d = []
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)

b = []
for i in range(n):
    b.append(list(map(int, sys.stdin.readline().split())))

for i, j in b:
    d[i][j] = 1

for i in range(1, len(d)):
    for j in range(1, len(d[0])):
        print(d[i][j], end=' ')
    print()