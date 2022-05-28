# https://www.acmicpc.net/problem/10828
import sys
input = sys.stdin.readline

n = int(input())

stack = []
for i in range(n):
    a = input().strip()
    if "push" in a:
        _, b = a.split()
        stack.append(int(b))
    elif a == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(f"{stack[-1]}")
    elif a == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif a == "size":
        print(len(stack))
    else:
        if len(stack) == 0:
            print(1)
        else:
            print(0)