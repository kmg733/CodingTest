# https://programmers.co.kr/learn/courses/30/lessons/12934
import math
def solution(n):
    if n == int(math.sqrt(n)) ** 2:
        answer = (int(math.sqrt(n)) + 1) ** 2
        return answer
    else:
        return -1