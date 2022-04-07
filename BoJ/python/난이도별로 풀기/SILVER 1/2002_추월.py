# https://www.acmicpc.net/problem/2002
import sys
input = sys.stdin.readline

n = int(input())

enter = dict()
for i in range(n):
    enter[input().strip()] = i

out = []
for _ in range(n):
    out.append(input().strip())

count = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if enter[out[i]] > enter[out[j]]:
            count += 1
            break
    
print(count)