# https://www.acmicpc.net/problem/16677
import sys
input = sys.stdin.readline

m = input().strip()
n = int(input())

d = []
for _ in range(n):
    a, b = map(str, input().split())
    a = "".join(a)
   
    index = 0
    for i in a:
        if i == m[index]:
            index += 1
            if index == len(m):
                index -= 1
        else:
            
    # 정답중 하나라면
    if index == len(m):   
        d.append([a, b/(len(a) - len(m))])


if len(d) == 0:
    print('No Jam')
else:
    print(d)