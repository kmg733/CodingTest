# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AWGsRbk6AQIDFAVW&categoryId=AWGsRbk6AQIDFAVW&categoryType=CODE&problemTitle=&orderBy=PASS_RATE&selectCodeLang=PYTHON&select-1=3&pageSize=30&pageIndex=2

t = int(input())

for case in range(1, t + 1):
    n = int(input())
    card = input().split()

    # 카드 갯수가 짝수 일 때
    if len(card) % 2 == 0:
        left = card[:len(card) // 2]
        right = card[len(card) // 2:]
    # 카드 갯수가 홀수 일 때
    else:
        left = card[:len(card) // 2 + 1]
        right = card[len(card) // 2 + 1:]
    
    for i in range(len(right)):
        left.insert(i * 2 + 1, right[i])
    
    print(f"#{case}", end=" ")
    print(*left)