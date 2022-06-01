# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWE_ZXcqAAMDFAV2&categoryId=AWE_ZXcqAAMDFAV2&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=30&pageIndex=1

t = int(input())

for case in range(1, t + 1):
    l, u, x = map(int, input().split())

    result = 0
    if x < l:
        result = l - x
    elif l <= x <= u:
        result = 0
    else:
        result = -1
    print(f"#{case} {result}")