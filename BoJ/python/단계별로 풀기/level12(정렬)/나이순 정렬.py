import sys

n = int(input())
lists = []

for i in range(n):
    age, name = sys.stdin.readline().split()
    lists.append([i, int(age), name])

lists.sort(key=lambda x:(x[1], x[0]))

for a, b ,c in lists:
    print(b, c)
