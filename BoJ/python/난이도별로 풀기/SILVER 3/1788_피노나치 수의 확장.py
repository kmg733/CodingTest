# https://www.acmicpc.net/problem/1788
import sys
input = sys.stdin.readline

n = int(input())
dp = [0, 1]

# 피보나치 음수 부분은 양수 부분과 값이 대칭 됨
# n에 절대값에 대한(양수) 피보나치를 구하고 n값에 따라 출력을 하면 됨
for i in range(2, abs(n) + 1):
    dp.append((dp[i - 1] + dp[i - 2]) % 1000000000)
 
if n % 2 == 0 and n < 0:
    print(-1)
elif n == 0:
    print(0)
else:
    print(1)

print(dp[abs(n)])