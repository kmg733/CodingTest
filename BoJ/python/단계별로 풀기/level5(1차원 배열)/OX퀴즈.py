import sys

n = int(input())
a = []

for i in range(n):
    cnt = 1
    sum = 0
    a.append(sys.stdin.readline().strip())
    for j in a[i]:
        if j == 'O':
            sum += cnt
            cnt += 1
        else:
            cnt = 1
    print(sum)
