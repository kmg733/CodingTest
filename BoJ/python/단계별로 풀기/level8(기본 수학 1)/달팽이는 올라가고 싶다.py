import sys
import math
a, b, v = map(int, sys.stdin.readline().split())

date = (v - b) / (a - b)
print(math.ceil(date))