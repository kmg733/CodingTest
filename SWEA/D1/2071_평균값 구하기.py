# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QRnJqA5cDFAUq&categoryId=AV5QRnJqA5cDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1
import sys
input = sys.stdin.readline

T = int(input())
for i in range(1, T + 1):
    ary = list(map(int, input().split()))
    print(f"#{i} {round(sum(ary) / len(ary))}")