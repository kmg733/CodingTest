# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QQ6qqA40DFAUq&categoryId=AV5QQ6qqA40DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1
import sys
input = sys.stdin.readline

T = int(input())
for i in range(1, T + 1):
    a, b = map(int, input().split())
    if a > b:
        result = '>'
    elif a < b:
        result = '<'
    else:
        result = '='
    print(f"#{i} {result}")