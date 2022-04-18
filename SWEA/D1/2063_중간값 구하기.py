# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QPsXKA2UDFAUq&categoryId=AV5QPsXKA2UDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1
import sys
input = sys.stdin.readline

n = int(input())
ary = list(set(map(int, input().split())))
ary.sort()
print(f"{ary[len(ary) // 2 + 1]}")