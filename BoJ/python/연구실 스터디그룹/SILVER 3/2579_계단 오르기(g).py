# https://www.acmicpc.net/problem/2579
import sys
input = sys.stdin.readline

n = int(input())
# DP 테이블(i번째 계단까지의 최대값 저장)
d = [0] * 301
# i번째 계단의 점수
stair = []
for i in range(n):
    stair.append(int(input()))    

if n > 2:
    # 상향식
    d[0] = stair[0]
    d[1] = max(stair[0] + stair[1], stair[1])
    d[2] = max(stair[0] + stair[2], stair[1] + stair[2]) 
    for i in range(3, n):
        # 한칸 건너뛰어서 계단을 밟은 경우과 직전의 계단을 밟은 경우를 비교하여 큰값을 넣음
        d[i] = max(d[i - 2] + stair[i], d[i - 3] + stair[i] + stair[i - 1])    

    print(d[n - 1])
else:
    if n == 1:
        print(stair[0])
    elif n == 2:
        print(max(stair[0] + stair[1], stair[1]))
# 참고 : https://sungmin-joo.tistory.com/18
# DP