# https://www.acmicpc.net/problem/6236
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dMoney = [int(input()) for _ in range(n)]

def binary(start, end):
    if start > end:
        return end + 1
    
    # 인출할 돈
    mid = (start + end) // 2
    # 현재 가진 돈
    cMoney = mid
    # 날짜
    day = 1

    for money in dMoney:
        # 현재 가진돈이 사용할 돈보다 적으면 충전
        if cMoney < money:
            cMoney = mid
            day += 1
        # 현재돈에서 오늘 할당된 금액 사용
        cMoney -= money

    if day > m or mid < max(dMoney):
        return binary(mid + 1, end)
    else:
        return binary(start, mid - 1)                
        
print(binary(min(dMoney), sum(dMoney)))

# 참고: https://yeoooo.github.io/algorithm/BOJ6236/

# 이진 탐색