# https://programmers.co.kr/learn/courses/30/lessons/17681
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        result = bin(arr1[i] | arr2[i])
        result = result.lstrip('0b')

        add0 = ''
        while len(result) + len(add0) < n:
            add0 += '0'
        result = add0 + result
        result = result.replace('1', '#')
        result = result.replace('0', ' ')
        answer.append(result)

    return answer

# 다른 사람의 풀이
# def solution(n, arr1, arr2):
#     answer = []
#     for i,j in zip(arr1,arr2):
#         a12 = str(bin(i|j)[2:])
#         a12=a12.rjust(n,'0')
#         a12=a12.replace('1','#')
#         a12=a12.replace('0',' ')
#         answer.append(a12)
#     return answer

# 참고
# https://www.crocus.co.kr/1660