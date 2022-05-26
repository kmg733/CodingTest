# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV13zo1KAAACFAYh&categoryId=AV13zo1KAAACFAYh&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=1
from collections import Counter

t = int(input())

for case in range(1, t + 1):
    input()
    ary = list(map(int, input().split()))
    ary.sort(reverse = True)
    result = Counter(ary)
    print(f"#{case} {result.most_common(1)[0][0]}")
