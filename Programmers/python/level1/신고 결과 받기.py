# https://programmers.co.kr/learn/courses/30/lessons/92334?language=python3
from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reportCount = defaultdict(int)
    reportWho = defaultdict(list)

    # 중복제거
    report = list(set(report))

    suspend = []
    for str in report:
        reportFrom, reportTo = str.split()
        reportWho[reportFrom].append(reportTo)
        reportCount[reportTo] += 1

        if reportCount[reportTo] == k:
            suspend.append(reportTo)
    
    for sus in suspend:
        for i in range(len(id_list)):
            if sus in reportWho[id_list[i]]:
                answer[i] += 1

    return answer

# 다른 사람의 풀이
# def solution(id_list, report, k):
#     answer = []
#     a = list(set(report))
#     dictionary2 = {name : 0 for name in id_list}
#     dictionary = {name : [] for name in id_list}
#     for i in a:
#         dictionary[i.split()[1]].append(i.split()[0])
#     print(dictionary)
#     for i in dictionary:
#         print(i)
#         if len(dictionary[i]) >= k:
#             for j in dictionary[i]:
#                 dictionary2[j] += 1

#     for i in dictionary2:
#         answer.append(dictionary2[i])

#     return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list, report, k))