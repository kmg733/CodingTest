# https://programmers.co.kr/learn/courses/30/lessons/12931
def solution(n):
    answer = 0
    for i in list(str(n)):
        answer += int(i)   
    return answer
# 다른 사람의 풀이
# def solution(n):
#     return sum(map(int,str(n)))