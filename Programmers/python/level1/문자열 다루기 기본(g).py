# https://programmers.co.kr/learn/courses/30/lessons/12918
def solution(s):
    if len(s) == 4 or len(s) == 6:
        return s.isdigit()
    else:
        return False
# 다른 사람의 풀이
# def alpha_string46(s):
#     try:
#         int(s)
#     except:
#         return False
#     return len(s) == 4 or len(s) == 6 

# 참고 isalpha, isdigit, isalnum 사용법
# https://appia.tistory.com/178