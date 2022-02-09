# https://www.acmicpc.net/problem/22233
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

memo = {}
for i in range(n):
    memo[input().strip()] = i

for i in range(m):
    useWords = list(map(str, input().rstrip().split(",")))
    for word in useWords:
        if word in memo.keys():
            del memo[word]
    print(len(memo))    
