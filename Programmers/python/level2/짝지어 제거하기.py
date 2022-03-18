# https://programmers.co.kr/learn/courses/30/lessons/12973
# 시간초과 답
def solution2(s):
    flag = True
    answer = 0
    while flag:
        if len(s) == 0:
            answer = 1
            break
            
        temp = '?'
        s = list(s)
        for idx, c in enumerate(s):
            if c == temp:
                del s[idx - 1:idx + 1]
                break
            
            if idx == len(s) - 1:
                flag = False
            temp = c
    
    return answer

def solution(s):
    stack = []
    for c in s:
        if len(stack) == 0:
            stack.append(c)
        else:
            if c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
    
    if len(stack) == 0:
        return 1
    else:
        return 0