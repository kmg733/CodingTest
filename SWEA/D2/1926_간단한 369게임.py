# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PTeo6AHUDFAUq&categoryId=AV5PTeo6AHUDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=1
n = int(input())

result = ''
for i in range(1, n + 1):
    num = str(i)
    count = num.count('3') + num.count('6') + num.count('9')
    if count > 0:
        result += '-' * count + ' '
    else:
        result += num + ' '
    
print(result)