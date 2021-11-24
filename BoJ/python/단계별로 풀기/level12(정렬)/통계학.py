# 최빈값을 구할 때 Counter 메소드를 안쓰면 시간초과 발생

import sys
from collections import Counter

n = int(input())
num = []

for _ in range(n):
    num.append(int(sys.stdin.readline()))
num.sort()

print(round(sum(num) / n))

print(num[n // 2])

cnt = Counter(num).most_common()    # [(값, 횟수), (값, 횟수)]
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])

print(max(num) - min(num))