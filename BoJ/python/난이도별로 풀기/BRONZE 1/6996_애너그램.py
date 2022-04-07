# https://www.acmicpc.net/problem/6996
import sys

n = int(sys.stdin.readline())

for i in range(n):
    a, b = map(str, sys.stdin.readline().split())

    x = sorted(list(a))
    y = sorted(list(b))

    if x == y:
        print('%s & %s are anagrams.' %(a, b))
    else:
        print('%s & %s are NOT anagrams.' %(a, b))