# https://programmers.co.kr/learn/courses/30/lessons/12922
def solution(n):
    if n % 2 == 0:
        answer = '수박' * (n // 2)
    else:
        answer = '수박' * (n // 2) + '수'
    return answer

# 다른 사람의 풀이
# def solution(n):
#     return "수박"*(n//2) + "수"*(n%2)