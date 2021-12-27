# https://www.acmicpc.net/problem/16677
import sys
input = sys.stdin.readline

m = input().strip()
n = int(input())

d = []
for _ in range(n):
    a, b = input().split()
    b = int(b)

    # 길이가 작거나 같은 문자가 들어올 경우 예외처리
    if len(m) >= len(a):
        continue
    else:
        # 해당 문자가 No Jam인지 체크
        chk = 0
        for i in range(len(m)):
            if m.count(m[i]) > a.count(m[i]):
                break
            chk += 1

        # No Jam인경우 확인할 필요가 없으니 continue
        if chk != len(m):
            continue
        
        # m과 a가 같을경우
        cost = b / (len(a) - len(m))        
        d.append([a, cost])
    
# 조건에 해당하는 문자가 없을경우 d의 길이가 0
if len(d) == 0:
    print('No Jam')
else:
    # d[1]기준으로 내림차순 정렬을 한다.
    # sort의 특성상 같은 값의 경우는 정렬하지 않기 때문에
    # 더 빠른 인덱스를 가지는 값이 앞에오게 된다.
    d.sort(key=lambda x:-x[1])
    print(d[0][0])


# m = input()
# n = int(input())

# result = 'No Jam'
# result_g = 0

# for i in range(n):
#     w, g = input().split()
#     g = int(g)
#     if len(m) >= len(w):
#         continue
#     m_stack = list(reversed(m))
#     w_stack = list(w)
#     for j in w_stack:
#         if m_stack[-1] == j:
#             m_stack.pop()
#         if len(m_stack) == 0:
#             g /= (len(w) - len(m))
#             if g > result_g:
#                 result = w
#                 result_g = g
#             break
# print(result)