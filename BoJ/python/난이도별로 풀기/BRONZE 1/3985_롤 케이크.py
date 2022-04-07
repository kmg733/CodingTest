# https://www.acmicpc.net/problem/3985
from collections import Counter
from collections import defaultdict
import sys
input = sys.stdin.readline

l = int(input())
cake = defaultdict(int)

n = int(input())
maxCake = 0
maxCakeIdx = -1
for i in range(1, n + 1):
    p, k = map(int, input().split())

    # maxCakeIdx에 가장 많은 조각을 받을 것으로 기대하는 방청객의 번호 저장
    if maxCake < k - p:
        maxCakeIdx = i
        maxCake = k - p

    for c in range(p, k + 1):
        if cake[c] == 0:
            cake[c] = i

print(maxCakeIdx)
print(Counter(cake.values()).most_common(1)[0][0])