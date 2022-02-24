from collections import Counter

def solution(N, stages):
    counts = Counter(stages)
    result = {}
    total = len(stages)
    for i in range(1, N + 1):        
        if total != 0:
            count = counts[i]
            result[i] = count / total
            total -= count
        else:
            result[i] = 0
    return sorted(result, key=lambda x : -result[x])

# 다른사람의 풀이
# def solution(N, stages):
#     result = {}
#     denominator = len(stages)
#     for stage in range(1, N+1):
#         if denominator != 0:
#             count = stages.count(stage)
#             result[stage] = count / denominator
#             denominator -= count
#         else:
#             result[stage] = 0
#     return sorted(result, key=lambda x : result[x], reverse=True)

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))