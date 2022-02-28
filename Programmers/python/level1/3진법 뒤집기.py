def solution(n):
    answer = ''
    while n > 0:
        n, mod = divmod(n, 3)
        answer += str(mod)
    print(answer.lstrip('0'))
    return int(answer, 3)