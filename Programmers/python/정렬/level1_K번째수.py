# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for i in commands:
        arr = array[i[0]-1:i[1]]
        arr.sort()
        answer.append(arr[i[2]-1])
    return answer

a = [1, 5, 2, 6, 3, 7, 4]
b = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(a, b))

# 더 간결한 코드

# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

# lambda의 사용방법 : https://dojang.io/mod/page/view.php?id=2359