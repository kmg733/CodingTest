# https://www.acmicpc.net/problem/1874
import sys
input = sys.stdin.readline

n = int(input())
count = 0
stack = []
result = []

# 입력
inp = []
for i in range(n):
    inp.append(int(input()))

for x in inp:
    while count < x:
        count += 1
        stack.append(count)
        result.append("+")
    
    # 찾는 값이면 pop
    if stack[-1] == x:
        stack.pop()
        result.append("-")
    # 찾는 값이 아니면 수열을 만들 수 없으므로 break
    else:
        print("NO")
        break

# break가 걸리지 않으면 실행
else:
    for r in result:
        print(r)