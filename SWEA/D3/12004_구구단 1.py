# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXkcWgFa8sADFAS8&categoryId=AXkcWgFa8sADFAS8&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=30&pageIndex=2

from itertools import combinations_with_replacement

t = int(input())
ary = []
for i in range(1, 10):
    ary.append(i)

result = []
for a, b in combinations_with_replacement(ary, 2):
    result.append(a * b)

result = list(set(result))

for case in range(1, t + 1):
    n = int(input())

    if n not in result:
        print(f"#{case} No")
    else:
        print(f"#{case} Yes")
        