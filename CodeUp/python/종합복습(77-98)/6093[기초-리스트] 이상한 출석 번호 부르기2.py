import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

for i in range(n-1, -1, -1):
    print(a[i], end=' ')