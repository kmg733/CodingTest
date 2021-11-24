import sys

h, b, c, s = map(float, sys.stdin.readline().split())
cal = (h * b * c * s) / 8 / 1024 / 1024
print('%.1f'%cal, 'MB')