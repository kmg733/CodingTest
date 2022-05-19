# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PxmBqAe8DFAUq&categoryId=AV5PxmBqAe8DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=1

t = int(input())

for i in range(1, t + 1):
    n = int(input())
    if n % 2 != 0:
        print(f"#{i} {(n + 1) // 2}")
    else:
        print(f"#{i} {(n // 2) * -1}")