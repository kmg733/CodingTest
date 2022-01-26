# https://www.acmicpc.net/problem/9375
import sys
input = sys.stdin.readline

# 경우의 수를 따지면 풀리는 문제이다.
# 옷이 없는경우 까지 포함하여 센다.

t = int(input())
for _ in range(t):
    n = int(input())    

    cloth = dict()
    for _ in range(n):
        a, b = input().split()
        if b not in cloth:
            cloth[b] = 1
        else:
            cloth[b] += 1

    result = 1
    for value in cloth.values():
        result *= (value + 1)
    print(result - 1)

# 수학
# 자료 구조
# 조합론
# 해시를 사용한 집합과 맵
