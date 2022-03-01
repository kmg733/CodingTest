# https://programmers.co.kr/learn/courses/30/lessons/12912
def solution(a, b):    
    result = 0
    if a < b:        
        for i in range(a, b + 1):
            result += i
    elif a > b:
        for i in range(b, a + 1):
            result += i
    else:
        result = a            
    return result

# 다른 사람의 풀이
# def adder(a, b):     
#     if a > b: a, b = b, a
#     elif a == b: return a
#     return sum(range(a,b+1))