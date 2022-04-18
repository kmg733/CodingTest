# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QQhbqA4QDFAUq&categoryId=AV5QQhbqA4QDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1
import sys
input = sys.stdin.readline

T = int(input())
for i in range(1, T + 1):
    ary = list(map(int, input().split()))
    print(f"#{i} {max(ary)}")