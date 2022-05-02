# https://www.acmicpc.net/problem/1010
import sys, math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    # 수학의 조합을 이용한 풀이
    # 수학의 조합 공식 mCn 으로 구하면 됨
    # 이는 math 라이브러리의 comb로 구현되어 있음
    # print(math.comb(m, n))
 
    # DP 테이블 이용한 풀이
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 첫 행은 1 ~ m까지 초기화
            if i == 1:
                dp[i][j] = j            
        
            # 점화식 : dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
    print(dp[n][m])