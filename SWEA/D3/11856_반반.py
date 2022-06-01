# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXjS1GXqZ8gDFATi&categoryId=AXjS1GXqZ8gDFATi&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=30&pageIndex=2
# from collections import Counter
from collections import defaultdict

t = int(input())

for case in range(1, t + 1):
    s = input().strip()
    dict = defaultdict(int)

    for c in s:
        dict[c] += 1

    result = "Yes"
    if len(dict) == 2:
        for v in dict.values():
            if v != 2:
                result = "No"
                break
    else:
        result = "No"
    
    print(f"#{case} {result}")
