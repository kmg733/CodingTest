import sys 

n = int(input())
a = list(map(int, sys.stdin.readline().split()))
max = a[0]
min = a[0]
# a.sort()
# print(a[0], a[-1])

for i in a[1:]:
    if i > max:
        max = i
    elif i < min:
        min = i

print(min, max)