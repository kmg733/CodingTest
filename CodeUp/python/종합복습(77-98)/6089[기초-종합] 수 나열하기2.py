import sys

a, r, n = map(int, sys.stdin.readline().split())

result = a * (r ** (n-1))
print(result)