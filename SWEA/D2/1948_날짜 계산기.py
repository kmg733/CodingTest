# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PnnU6AOsDFAUq&categoryId=AV5PnnU6AOsDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=1
import datetime
t = int(input())

for case in range(1, t + 1):
    m1, d1, m2, d2 = map(int, input().split())
    days1 = datetime.date(2022, m1, d1)
    days2 = datetime.date(2022, m2, d2)
    result = days2 - days1
    print(f"#{case} {result.days + 1}")