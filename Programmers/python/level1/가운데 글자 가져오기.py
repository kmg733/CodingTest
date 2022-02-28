# https://programmers.co.kr/learn/courses/30/lessons/12903
def solution(s):
    lens = len(s)
    if lens % 2 == 0:
        return s[lens // 2 - 1:lens // 2 + 1]
    else:
        return s[lens // 2]