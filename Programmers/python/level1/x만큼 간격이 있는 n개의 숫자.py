# https://programmers.co.kr/learn/courses/30/lessons/12954
def solution(x, n):
    if x > 0:
        answer = [i for i in range(x, x * n + 1, x)]
    elif x < 0:
        answer = [i for i in range(x, x * n - 1, x)]
    else:
        answer = [0] * n
    return answer

# 다른 사람의 풀이
# def solution(x, n):
#     answer = [x * i + x for i in range(n)] 
#     return answer