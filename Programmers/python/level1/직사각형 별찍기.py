# https://programmers.co.kr/learn/courses/30/lessons/12969
import sys
input = sys.stdin.readline

a, b = map(int, input().strip().split(' '))
for i in range(b):
    for j in range(a):
        print('*', end='')
    print()