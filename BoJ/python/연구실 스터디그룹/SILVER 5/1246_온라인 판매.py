# https://www.acmicpc.net/problem/1246
import sys

N, M = map(int, sys.stdin.readline().split())
P = []
for i in range(M):
    P.append(int(sys.stdin.readline()))

P.sort()
dict = {}
for i in range(len(P)):
    if len(P[i:]) > N:
        dict[N * P[i]] = P[i]
    else:
        dict[len(P[i:]) * P[i]] = P[i]

p = max(dict.keys())
print(dict[p], p)

# sum = [0]*M
# for i in range(M):
#     s = P[i]
#     lim = N
#     for j in range(M):
#         if P[j] >= s:
#             if lim > 0:
#                 sum[i] += s
#                 lim -= 1
# print(P[sum.index(max(sum))], max(sum))