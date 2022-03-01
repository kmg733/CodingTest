# https://programmers.co.kr/learn/courses/30/lessons/12915
def solution(strings, n):
    strings.sort()
    answer = sorted(strings, key=lambda x: x[n])
    return answer

# 다른 사람의 풀이
# def solution(strings, n):
#     answer = sorted(strings, key=lambda x: (x[n], x))
#     return answer

# 역순 정렬
# def solution(strings, n):
#     strings.sort(reverse = True)
#     answer = sorted(strings, key=lambda x: (x[n]))
#     return answer

print(solution(["abce", "abcd", "cdx", 'abcf'], 1))