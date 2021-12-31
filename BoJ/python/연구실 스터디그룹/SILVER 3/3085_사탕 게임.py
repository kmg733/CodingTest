# https://www.acmicpc.net/problem/3085
import sys
input = sys.stdin.readline

def checkMax(l):
    maxC = 0
    count = 0
    # 행
    for i in range(len(l)):        
        chr = '?'
        for j in range(len(l[0])):
            if chr != l[i][j]:
                chr = l[i][j]
                maxC = max(maxC, count)
                count = 1
            else:
                count += 1
    
    # 열
    for i in range(len(l[0])):
        chr = '?'
        for j in range(len(l)):
            if chr != l[j][i]:
                chr = l[j][i]
                maxC = max(maxC, count)
                count = 1
            else:
                count += 1
    
    return maxC

n = int(input())

candy = []
for i in range(n):
    candy.append(list(input().strip()))

candyCopy = candy
maxC = 0

# 행 바꾸기
for i in range(len(candyCopy)):
    for j in range(len(candyCopy[0])-1):
        if candyCopy[i][j] != candyCopy[i][j+1]:
                # 다른 2개 바꾸기
                temp = candyCopy[i][j]
                candyCopy[i][j] = candyCopy[i][j+1]
                candyCopy[i][j+1] = temp

                maxC = max(maxC, checkMax(candyCopy))

                # 원상 복구
                temp = candyCopy[i][j]
                candyCopy[i][j] = candyCopy[i][j+1]
                candyCopy[i][j+1] = temp

# 열 바꾸기
for i in range(len(candyCopy[0])):
    for j in range(len(candyCopy)-1):
        if candyCopy[j][i] != candyCopy[j+1][i]:
                # 다른 2개 바꾸기
                temp = candyCopy[j][i]
                candyCopy[j][i] = candyCopy[j+1][i]
                candyCopy[j+1][i] = temp

                maxC = max(maxC, checkMax(candyCopy))

                # 원상 복구
                temp = candyCopy[j][i]
                candyCopy[j][i] = candyCopy[j+1][i]
                candyCopy[j+1][i] = temp
print(maxC)