# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PwGK6AcIDFAUq&categoryId=AV5PwGK6AcIDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=1

t = int(input())
grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"] 

for i in range(1, t + 1):
    n, k = map(int, input().split())
    student = []

    for j in range(n):
        middle, final, assignment = map(int, input().split())
        total = middle * 0.35 + final * 0.45 + assignment * 0.2
        student.append(total)

    temp = student[k - 1]
    student.sort(reverse=True)
    result = grade[student.index(temp) // (n // 10)]
    print(f"#{i} {result}")