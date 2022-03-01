# https://programmers.co.kr/learn/courses/30/lessons/12928
def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if n % i == 0:
            answer += i
    return answer

# def solution(n):
#     answer = 0
#     for i in range(1, n // 2 + 1):
#         if n % i == 0:
#             answer += i
#     answer += n
#     return answer

# 다른 사람의 풀이
# def solution(num):
#     # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
#     return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])