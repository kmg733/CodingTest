# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5Pl0Q6ANQDFAUq&categoryId=AV5Pl0Q6ANQDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=1
from collections import defaultdict 

t = int(input())
soinsu = ["11", "7", "5", "3", "2"]
for case in range(1, t + 1):
    n = int(input())
    result = defaultdict(int)

    while n != 1:
        for s in soinsu:
            if n % int(s) == 0:
                n = n // int(s)
                result[s] += 1
                break
    print(f"#{case} {result['2']} {result['3']} {result['5']} {result['7']} {result['11']}")


t = int(input())
for case in range(1, t + 1):
    n = int(input())
    result = [0] * 5

    while n % 2 == 0:
        result[0] += 1
        n //= 2

    while n % 3 == 0:
        result[1] += 1
        n //= 3

    while n % 5 == 0:
        result[2] += 1
        n //= 5

    while n % 7 == 0:
        result[3] += 1
        n //= 7

    while n % 11 == 0:
        result[4] += 1
        n //= 11

    print(f"#{case}", end = " ")
    print(*result)