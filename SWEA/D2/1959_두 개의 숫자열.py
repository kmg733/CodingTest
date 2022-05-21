# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PpoFaAS4DFAUq&categoryId=AV5PpoFaAS4DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=1

t = int(input())
for case in range(1, t + 1):
    n, m = map(int, input().split())    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # 항상 a가 크게
    if n < m:
        temp = a
        a = b
        b = temp

    answer = 0
    for i in range(len(a) - len(b) + 1):
        maxNum = 0
        for j in range(len(b)):
            maxNum += a[i + j] * b[j]
        answer = max(answer, maxNum)
        
    print(f"#{case} {answer}")