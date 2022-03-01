# https://programmers.co.kr/learn/courses/30/lessons/12933
def solution(n):
    l = list(str(int(n)))
    l.sort(reverse = True)
    return int(''.join(l))

print(solution(1))