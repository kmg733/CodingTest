# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QSEhaA5sDFAUq&categoryId=AV5QSEhaA5sDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=1
import sys
input = sys.stdin.readline

T = int(input())
for i in range(1, T + 1):
    ary = list(map(int, input().split()))
    sum = 0
    for a in ary:
        if a % 2 == 1:
            sum += a
    print(f"#{i} {sum}")