# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5PjKXKALcDFAUq&categoryId=AV5PjKXKALcDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=1&pageSize=30&pageIndex=1
a, b = map(int, input().split())
if a == 1:
    if b == 2:
        print("B")
    else:  
        print("A")
elif a == 2:
    if b == 1:
        print("A")
    else:
        print("B")
elif a == 3:
    if b == 1:
        print("B")
    else:
        print("A")
