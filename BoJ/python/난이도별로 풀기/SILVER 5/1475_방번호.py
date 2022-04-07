#https://www.acmicpc.net/problem/1475
import sys

n = str(sys.stdin.readline().strip())

a = []
for i in range(10):
    a.append(n.count(str(i)))

if (a[6] + a[9]) % 2 == 1:
    a[6] = (a[6] + a[9] + 1) // 2
else:
    a[6] = (a[6] + a[9]) // 2
a[9] = 0
print(max(a))