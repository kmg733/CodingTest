# https://www.acmicpc.net/problem/11047
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))

count = 0
for c in coin[::-1]:
    count += k // c
    k = k % c

print(count)