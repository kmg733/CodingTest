# https://www.acmicpc.net/problem/2869
import sys, math

a, b, v = map(int, sys.stdin.readline().split())

day = (v - b) / (a - b)
print(math.ceil(day))