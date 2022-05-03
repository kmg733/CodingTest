# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5P1kNKAl8DFAUq&categoryId=AV5P1kNKAl8DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=1
n = int(input())
for i in range(1, n + 1):
    s = input()

    for j in range(1, 11):
        cut1 = s[:j]
        cut2 = s[j: j * 2]
        if cut1 == cut2:
            result = len(cut1)
            break
    
    print(f"#{i} {result}")