# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV189xUaI8UCFAZN&categoryId=AV189xUaI8UCFAZN&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=1

t = int(input())

for case in range(1, t + 1):
    p, q, r, s, w = map(int, input().split())

    # A사
    aCost = w * p

    # B사
    if w > r:
        bCost = (w - r) * s + q
    else:
        bCost = q 

    if aCost > bCost:
        print(f"#{case} {bCost}")
    else:
        print(f"#{case} {aCost}")
