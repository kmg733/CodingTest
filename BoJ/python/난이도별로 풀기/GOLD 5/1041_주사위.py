# https://www.acmicpc.net/problem/1041
import sys
input = sys.stdin.readline

# 주사위 모습
#     +---+        
#     | D |        
# +---+---+---+---+
# | E | A | B | F |
# +---+---+---+---+
#     | C |        
#     +---+        
# 면이 1개 보이는 블록 개수 : 4 * (N - 2) * (N - 1) + (N - 2) ** 2   
# 면이 2개 보이는 블록 개수 : 4 * (N - 1) + 4 * (N - 2)
# 면이 3개 보이는 블록 개수 : 4 (가장 상단 모서리 4개)

n = int(input())
ary = list(map(int, input().split()))
result = 0
minList = []

# 크기(갯수)가 1인 주사위
if n == 1:
    ary.sort()
    for i in range(5):
        result += ary[i]

# 크기(갯수)가 1이 아닌 주사위
else:
    # 마주보는 숫자중 작은것 추가
    minList.append(min(ary[0], ary[5]))
    minList.append(min(ary[1], ary[4]))
    minList.append(min(ary[2], ary[3]))
    minList.sort()

    # 주사위 갯수
    diceCount1 = 4 * (n - 2) * (n - 1) + (n - 2) ** 2
    diceCount2 = 4 * (n - 1) + 4 * (n - 2)
    diceCount3 = 4

    # 면에 보여줄 숫자 3개
    diceValue1 = minList[0]
    diceValue2 = minList[0] + minList[1]
    diceValue3 = sum(minList)

    result += diceCount1 * diceValue1
    result += diceCount2 * diceValue2
    result += diceCount3 * diceValue3

print(result)

# 그리디 알고리즘