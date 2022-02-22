# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    answer = []
    worst = 0

    for num in lottos:
        if num in win_nums:
            worst += 1

    answer.append(answerApeend(worst + lottos.count(0)))
    answer.append(answerApeend(worst))

    return answer

def answerApeend(num):
    result = -1
    if num == 6:
        return 1
    elif num == 5:
        result = 2
    elif num == 4:
        result = 3
    elif num == 3:
        result = 4
    elif num == 2:
        result = 5
    else:
        result = 6    
    return result

# 다른 사람의 풀이
# def solution(lottos, win_nums):

#     rank=[6,6,5,4,3,2,1]

#     cnt_0 = lottos.count(0)
#     ans = 0
#     for x in win_nums:
#         if x in lottos:
#             ans += 1
#     return rank[cnt_0 + ans],rank[ans]

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))