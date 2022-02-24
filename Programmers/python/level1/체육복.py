

def solution(n, lost, reserve):
    answer = n
    lost.sort()
    reserve.sort()
    # 자신에게 여분이 있는 학생
    for i in range(1, n + 1):
        if i in lost:
            if i in reserve:
                reserve.remove(i)
                lost.remove(i)

    # 빌려야 하는 학생
    for l in lost:
        if l - 1 in reserve:
            reserve.remove(l - 1)
        elif l + 1 in reserve:
            reserve.remove(l + 1)
        else:
            answer -= 1
    return answer

# 다른 사람 풀이
# def solution(n, lost, reserve):
#     answer = 0
#     for i in range(1, n+1):
#         if i not in lost: #안 잃어버린 학생
#             answer += 1
#         else:
#             if i in reserve: #잃어버렸지만 여분도 있는 학생
#                 answer += 1
#                 reserve.remove(i)
#                 lost.remove(i)

#     for i in lost: #잃어버리고 여분도 없어서 빌려야 하는 학생
#         if i-1 in reserve:
#             answer += 1
#             reserve.remove(i-1)

#         elif i+1 in reserve:
#             answer += 1
#             reserve.remove(i+1)

#     return answer
n = 5
lost = [2,4]
reserve = [1,3,5]
print(solution(n, lost, reserve))