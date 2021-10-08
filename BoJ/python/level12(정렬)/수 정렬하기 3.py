import sys

n = int(sys.stdin.readline())
ary = [0] * 10001

for _ in range(n):
    num = int(sys.stdin.readline())
    ary[num] += 1

for i in range(10001):
    if ary[i] != 0:
        for j in range(ary[i]):
            print(i)