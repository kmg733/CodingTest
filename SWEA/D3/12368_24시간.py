# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXsEBlLqedsDFARX&categoryId=AXsEBlLqedsDFARX&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=30&pageIndex=1

t = int(input())

for case in range(1, t + 1):
    a, b = map(int, input().split())
    print(f"#{case} {(a + b) % 24}")