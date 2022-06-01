# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AX6PP9G6p1sDFAS9&categoryId=AX6PP9G6p1sDFAS9&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=3&pageSize=10&pageIndex=1

t = int(input())

for case in range(1, t + 1):
    s = input().strip()
    if s.count('x') < 8:
        print(f"#{case} YES")
    else:
        print(f"#{case} NO")