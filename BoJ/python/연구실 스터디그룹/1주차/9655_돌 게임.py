# https://www.acmicpc.net/problem/9655
import sys

n = int(sys.stdin.readline())

n = n % 6
if n % 2 == 1:
    print('SK')
else:
    print('CY')