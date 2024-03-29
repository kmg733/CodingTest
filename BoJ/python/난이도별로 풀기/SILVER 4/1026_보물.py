# https://www.acmicpc.net/problem/1026
import sys
input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = 0
for i in range(n):
    result += min(a) * max(b)
    a.pop(a.index(min(a)))
    b.pop(b.index(max(b)))

print(result)

# 그리디 알고리즘