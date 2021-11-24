import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

d = []
for i in range(24):
    d.append(0)

for i in range(n):
    d[a[i]] += 1

for i in range(1, 24):
    print(d[i], end=' ')