# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PR4DKAG0DFAUq&categoryId=AV5PR4DKAG0DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=1
import base64

t = int(input())

for case in range(1, t + 1):
    s = input().strip()
    result = base64.b64decode(s).decode('utf-8')
    print(f"#{case} {result}")