import sys

n = int(input())
a = list(map(int, sys.stdin.readline().split()))

m = max(a)
sum = 0
for i in range(n):
    a[i] = a[i]/m*100
    sum += a[i]

print(sum/n)
