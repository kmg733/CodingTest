# https://programmers.co.kr/learn/courses/30/lessons/12899
def solution(n):
    # 1부터 시작하는 3진법을 1, 2, 4로 표현하는 문제    
    num = ['1', '2', '4']
    result = ''
    while n > 0:
        n -= 1
        result += str(num[n % 3])
        n = n // 3

    return result[::-1]
