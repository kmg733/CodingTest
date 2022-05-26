# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV18_yw6I9MCFAZN&categoryId=AV18_yw6I9MCFAZN&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=1

t = int(input())

for case in range(1, t + 1):
    n = input().strip()

    s = set(list(n))
    result = int(n)
    while len(s) < 10:
        result += int(n)
        s.update(list(str(result)))

    print(f"#{case} {result}")