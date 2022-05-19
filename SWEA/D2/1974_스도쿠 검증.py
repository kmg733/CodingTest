# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5Psz16AYEDFAUq&categoryId=AV5Psz16AYEDFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=2&pageSize=30&pageIndex=1

t = int(input())

def check():   
    # 가로 확인
    for i in range(9):
        check = []
        for j in range(9):
            if sudoku[i][j] not in check:
                check.append(sudoku[i][j])
            else:
                return(0)                

    # 세로 확인
    for i in range(9):
        check = []
        for j in range(9):
            if sudoku[j][i] not in check:
                check.append(sudoku[j][i])
            else:
                return 0                

    # 사각형 확인
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            check = []

            for k in range(3):
                for l in range(3):
                    if sudoku[i+k][j+l] not in check:
                        check.append(sudoku[i+k][j+l])
                    else:
                        return 0

    return 1

for case in range(1, t + 1):
    sudoku = []
    for i in range(9):
        sudoku.append(list(map(int, input().split())))

    print(f"#{case} {check()}")