# https://www.acmicpc.net/problem/15652
import sys
input = sys.stdin.readline

def dfs(start):
    if len(r) == m:
        print(' '.join(map(str, r)))
        return
    
    for i in range(start, n+1):
        r.append(i)
        dfs(i)
        r.pop()

n, m = map(int, input().split())
r = []
dfs(1)

# 백 트래킹 문제
# 참고 : https://jiwon-coding.tistory.com/34