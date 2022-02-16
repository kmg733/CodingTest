# https://www.acmicpc.net/problem/11497
import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()

    maxL = 0
    for i in range(2, n):
        maxL = max(maxL, abs(l[i] - l[i - 2]))
    
    maxL = max(maxL, abs(l[0] - l[1]))

    print(maxL)
