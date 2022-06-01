# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWTaTDua3OoDFAVT&categoryId=AWTaTDua3OoDFAVT&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=30&pageIndex=2

t = int(input())

for case in range(1, t + 1):
    a, b, c = map(int, input().split())
    a, b = min(a, b), max(a, b)
    result = c // a
    result += (c % a) // b
    print(f"#{case} {result}")