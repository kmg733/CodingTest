# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PmkDKAOMDFAUq&categoryId=AV5PmkDKAOMDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=1

t = int(input())
for case in range(1, t + 1):
    n = int(input())
    s = ""
    for _ in range(n):
        c, m = input().split()
        s += c * int(m)
    
    print(f"#{case}")
    for i in range(0, len(s), 10):
        print(s[i:i + 10])