# https://www.acmicpc.net/problem/2109
import sys, heapq
input = sys.stdin.readline

n = int(input())

pd = []
for i in range(n):
    pd.append(list(map(int, input().split())))

# 날짜를 기준으로 오름차순 정렬
pd.sort(key = lambda x: x[1])

heap = []
for pay, day in pd:
    heapq.heappush(heap, pay)

    if day < len(heap):
        heapq.heappop(heap)

print(sum(heap))