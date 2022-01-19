# https://www.acmicpc.net/problem/10816
import sys
from collections import Counter

input = sys.stdin.readline

_ = int(input())
ns = sorted(map(int, input().split()))
_ = int(input())
ms = list(map(int, input().split()))

# Collections 라이브러리
c = Counter(ns)
for m in ms:
    if m in c:
        print(c[m], end=' ')
    else:
        print(0, end=' ')
        
# 해쉬 알고리즘

# hashmap = {}
# for n in ns:
#     if n in hashmap:
#         hashmap[n] += 1
#     else:
#         hashmap[n] = 1

# result = []
# for m in ms:
#     if m in hashmap:
#         print(hashmap[m], end=' ')
#     else:
#         result.append(print(0, end=' '))

# 이진탐색

# def binary(n, start, end):
#     if start > end:
#         return -1
#     mid = (start + end) // 2
#     if n == ns[mid]:
#         return ns[start:end+1].count(n)
#     elif n < ns[mid]:
#         return binary(n, start, mid - 1)
#     else:
#         return binary(n, mid + 1, end)


# nDic = dict()
# for n in ns:
#     start = 0
#     end = len(ns) - 1
#     if n not in nDic:
#         nDic[n] = binary(n, start, end)

# print(' '.join(str(nDic[x]) if x in nDic else '0' for x in ms))

# 이진 탐색