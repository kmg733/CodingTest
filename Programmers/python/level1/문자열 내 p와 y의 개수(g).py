# https://programmers.co.kr/learn/courses/30/lessons/12916
from collections import Counter
def solution(s):
    counts = Counter(s)
    if counts['p'] + counts['P'] == counts['y'] + counts['Y']:
        return True
    else:
        return False

# 다른 사람의 풀이
# def numPY(s):
#     # 함수를 완성하세요
#     return s.lower().count('p') == s.lower().count('y')