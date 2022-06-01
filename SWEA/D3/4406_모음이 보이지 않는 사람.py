# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWNcD_66pUEDFAV8&categoryId=AWNcD_66pUEDFAV8&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=30&pageIndex=1

t = int(input())

for case in range(1, t + 1):
    s = input().strip()
    s = s.replace("a", "")
    s = s.replace("e", "")
    s = s.replace("i", "")
    s = s.replace("o", "")
    s = s.replace("u", "")
    print(f"#{case} {s}")