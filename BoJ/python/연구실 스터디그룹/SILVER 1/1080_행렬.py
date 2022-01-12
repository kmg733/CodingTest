# https://www.acmicpc.net/problem/1080
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = []
b = []
count = 0

# 3x3 바꾸기
def reverse(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            a[i][j] = 1 - a[i][j]            

for i in range(n):
    a.append(list(map(int, (input().strip()))))

for i in range(n):
    b.append(list(map(int, (input().strip()))))

# 행렬 뒤의 2개는 뒤집을 수 없기 때문에 체크에서 2를 뺀다
for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]:
            reverse(i, j)
            count +=1

if a != b:
    print(-1)
else:
    print(count)