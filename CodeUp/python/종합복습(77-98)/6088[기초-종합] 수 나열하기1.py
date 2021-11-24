import sys

a, d, n = map(int, sys.stdin.readline().split())
r = a + d * (n-1)
print(r)