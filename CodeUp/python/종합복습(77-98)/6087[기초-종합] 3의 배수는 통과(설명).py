import sys

n = int(sys.stdin.readline())

for i in range(1, n+1):
    if i % 3 == 0:
        continue
    else:
        print(i, end=" ")