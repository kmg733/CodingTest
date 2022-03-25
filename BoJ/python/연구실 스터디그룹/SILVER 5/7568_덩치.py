# https://www.acmicpc.net/problem/7568
import sys
input =  sys.stdin.readline

grade = []
n = int(input())
for i in range(n):
    grade.append(list(map(int, input().split())))

for i in range(n):
    g = 1
    for j in range(n):
        if i == j:
            continue
        if grade[i][0] < grade[j][0] and grade[i][1] < grade[j][1]:
            g += 1 
    
    print(g, end=' ')