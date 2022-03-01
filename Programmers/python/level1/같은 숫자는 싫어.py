# https://programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer = []
    past = -1
    for idx, a in enumerate(arr):
        if past == a:
            continue
        else:
            answer.append(a)
            past = a
    return answer

# 다른 사람의 풀이
# def no_continuous(s):
#     a = []
#     for i in s:
#         if a[-1:] == [i]: continue
#         a.append(i)
#     return a