import sys
N, X = map(int, input().split())

a = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    if(a[i] < X):
        print(a[i], end=" ")