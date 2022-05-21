# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PjMgaALgDFAUq&categoryId=AV5PjMgaALgDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=1

t = int(input())
for case in range(1, t + 1):
    n = int(input())
    speed = 0
    result = 0
    for i in range(n):
        ary = list(map(int, input().split()))
        # 가속
        if ary[0] == 1:
            speed += ary[1]
        # 감속
        elif ary[0] == 2:
            speed -= ary[1]
        
        if speed < 0:
            speed = 0
        
        result += speed
    print(f"#{case} {result}")