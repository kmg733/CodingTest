# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AXO8QBw6Qu4DFAXS&categoryId=AXO8QBw6Qu4DFAXS&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=30&pageIndex=3

t = int(input())

for case in range(1, t + 1):
    n = int(input())

    count = 0
    ab = []
    for i in range(n):
        a, b = map(int, input().split())

        for na, nb in ab:
            if (a > na and b < nb) or (a < na and b > nb):
                count += 1

        ab.append([a, b])
    print(f"#{case} {count}")