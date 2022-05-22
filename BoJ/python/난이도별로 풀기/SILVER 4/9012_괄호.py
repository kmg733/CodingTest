# https://www.acmicpc.net/problem/9012
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    vps = list(input().strip())
    stack = []

    for v in vps:
        if v == '(':
            stack.append(v)
        # ')' 일 때
        else:
            # 스택이 비어있지 않으면
            if len(stack):
                stack.pop()
            # 스택이 비어 있다면
            else:
                print("NO")
                break
    # for break문법
    else:
        if stack:
            print("NO")
        else:
            print("YES")