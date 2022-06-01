# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWZ2IErKCwUDFAUQ&categoryId=AWZ2IErKCwUDFAUQ&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=30&pageIndex=2
from itertools import combinations

t = int(input())

for case in range(1, t + 1):
    ary = list(map(int, input().split()))

    result = set()
    for value in combinations(ary, 3):
        result.add(sum(value))
    result = list(result)
    result.sort(reverse=True)
    print(f"#{case} {result[4]}")