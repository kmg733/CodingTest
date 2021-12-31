# https://www.acmicpc.net/problem/2621
import sys
input = sys.stdin.readline


def check():
    count, maxNum = checkContinue() 

    # 5장의 카드 색깔이 모두 같을 떄
    if 5 in colors.values():        
        
        # 5장의 카드 숫자가 연속적일때
        if count == 5:
            result = 900 + maxNum
            return result
        # 카드 색깔만 모두 같을 떄
        else:
            result = 600 + maxNum
            return result

    # 4장의 숫자가 같을 때
    elif 4 in numCount:
        result = 800 + numCount.index(4)
        return result

    # 3장의 숫자가 같을 떄
    elif 3 in numCount:

        # 2장의 숫자가 같은걸 포함 했을 때
        if 2 in numCount:
            result = 700 + numCount.index(3) * 10 + numCount.index(2)
            return result

        # 그 외
        else:
            result = 400 + numCount.index(3)
            return result

    elif 2 in numCount:
        big = 0
        small = 0
        if numCount.count(2) == 2:
            small = numCount.index(2)
            big = numCount.index(2, small+1)
            result = 300 + big * 10 + small
            return result
        else:
            result = 200 + numCount.index(2)
            return result

    # 5장의 카드 숫자가 연속적일 때
    if count == 5:
        result = 500 + maxNum
        return result

    result = max(numList)
    return result + 100
    
    
# 5장의 카드 숫자가 연속적인지 확인
def checkContinue():
    maxNum = 0
    count = 0
    for index, numC in enumerate(numCount):
        
        if numC > 0:
            count += 1
            maxNum = max(maxNum, index)
        else:
            count = 0

        if count == 5:
            break
        
    return count, maxNum

numList = []
colors = {
    'R':0,
    'B':0,
    'Y':0,
    'G':0
}
numCount = [0 for _ in range(10)]

for _ in range(5):
    color, num = input().split()
    num = int(num)
    numList.append(num)
    colors[color] += 1
    numCount[num] += 1

print(check())