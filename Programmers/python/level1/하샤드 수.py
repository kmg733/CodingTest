# https://programmers.co.kr/learn/courses/30/lessons/12947
def solution(x):
    h = sum(list(map(int, str(x))))
    if x % h == 0:
        return True
    else:
        return False