import sys

w, h, b = map(int, sys.stdin.readline().split())
cal = w * h * b / 8 / 1024 / 1024
print('%.2f'%cal, 'MB')