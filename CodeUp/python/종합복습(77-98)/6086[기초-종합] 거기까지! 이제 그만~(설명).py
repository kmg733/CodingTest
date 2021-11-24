import sys

n = int(sys.stdin.readline())
s = 0
c = 1

while True:
    s += c
    c += 1
    if s >= n:
        break

print(s)
