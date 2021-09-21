h, w = map(int, input().split())
n = int(input())

a = []
for i in range(h):
    a.append([])
    for j in range(w):
        a[i].append(0)

for i in range(n):
    l, d, x, y = map(int ,input().split())
    if l > 0:
        #가로
        if d == 0:
            for j in range(l):
                if a[int(x) - 1][int(y) - 1 + j] == 0:
                    a[int(x) - 1][int(y) - 1 + j] = 1
        #세로
        elif d == 1:
            for j in range(l):
                if a[int(x) - 1 + j][int(y) - 1] == 0:
                    a[int(x) - 1 + j][int(y) - 1] = 1

for i in range(h):
    for j in range(w):
        print(a[i][j], end=' ')
    print()
