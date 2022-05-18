# https://www.acmicpc.net/problem/2609
import sys
input = sys.stdin.readline

a, b = map(int, input().split())

# 유클리드 호제법
# gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

gcd = gcd(a, b)
# lcm
lcm = a * b // gcd

print(gcd)
print(lcm)