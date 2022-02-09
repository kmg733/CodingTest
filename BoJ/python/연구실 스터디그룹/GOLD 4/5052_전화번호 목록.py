# https://www.acmicpc.net/problem/5052
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    diary = []
    for i in range(n):
        diary.append(input().strip())
    diary.sort()

    flag = True
    for i in range(n - 1):
        if diary[i] == diary[i + 1][:len(diary[i])]:
            flag = False
            break
    
    if flag:
        print("YES")
    else:
        print("NO")