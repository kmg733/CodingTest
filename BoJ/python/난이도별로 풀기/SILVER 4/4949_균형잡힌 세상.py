# https://www.acmicpc.net/problem/4949
import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == '.':
        break
    
    stack = []

    for c in s:
        if c == "(" or c == "[":
            stack.append(c)            
        elif c == ")":
            if len(stack) > 0:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append("-1")
                    break
            else:
                stack.append("-1")
                break
        elif c == "]":
            if len(stack) > 0:
                if stack[-1] == "[":
                    stack.pop()
                else:
                    stack.append("-1")
                    break
            else:
                stack.append("-1")
                break
    
    if stack:
        print("no")
    else:
        print("yes")