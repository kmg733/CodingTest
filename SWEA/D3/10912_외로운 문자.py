# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXVJuEvqLAADFASe&categoryId=AXVJuEvqLAADFASe&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=30&pageIndex=2

t = int(input())

for case in range(1, t + 1):
    s = list(input().strip())

    result = []
    for c in s:
        if s.count(c) % 2 == 1:
            result.append(c)

    result = list(set(result))
    result.sort()

    if len(result) == 0:
        print(f"#{case} Good")
    else:
        print(f"#{case} {''.join(result)}")
