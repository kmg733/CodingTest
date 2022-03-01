# https://programmers.co.kr/learn/courses/30/lessons/12930
def solution(s):
    idx = 0
    word = list(s)
    for i, w in enumerate(word):
        # 알파벳인 경우
        if w.isalpha():
            # 짝수
            if idx % 2 == 0:
                word[i] = w.upper()
            # 홀수
            else:
                word[i] = w.lower()
            idx += 1
        # 공백인 경우
        else:
            idx = 0
    return ''.join(word)

print(solution("a aa  asdad"))

# 다른 사람의 풀이
# def solution(s):
#     a=[]
#     s=s.split(" ")
#     for i in range(len(s)):
#         for j in range(len(s[i])):
#             if j%2==0:
#                 a.append(s[i][j].upper())
#             else:
#                 a.append(s[i][j].lower())
#         a.append(" ")

#     c="".join(a[:-1])
#     return c
