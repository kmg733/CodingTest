# https://programmers.co.kr/learn/courses/30/lessons/12932
def solution(n):
    answer = reversed(list(str(n)))
    return list(map(int,answer))

# 다른 사람의 풀이
# def digit_reverse(n):
#     return list(map(int, reversed(str(n))))