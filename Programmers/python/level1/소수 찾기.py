# https://programmers.co.kr/learn/courses/30/lessons/12921
import math
def solution(n):
    answer = 1
    for i in range(3, n + 1):
        for j in range(2, int(math.sqrt(i)) + 1):
            # 소수가 아닌경우
            if i % j == 0:
                answer -= 1
                break
        answer += 1
    return answer

# 다른 사람의 풀이(에라토스테네스의 체)
# def solution(n):
#     num=set(range(2,n+1))

#     for i in range(2,n+1):
#         if i in num:
#             num-=set(range(2*i,n+1,i))
#     return len(num)