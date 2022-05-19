# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PttaaAZIDFAUq&categoryId=AV5PttaaAZIDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=1

t = int(input())
for case in range(1, t + 1):
    h1, m1, h2, m2 = map(int, input().split())
    h3 = h1 + h2 + (m1 + m2) // 60
    m3 = (m1 + m2) % 60

    if h3 > 12:
        h3 -= 12

    print(f"#{case} {h3} {m3}")