import sys

f = []
for i in range(10):
    f.append(list(map(int, sys.stdin.readline().split())))

x, y = 1, 1

while True:
    if f[x][y] == 0:
        f[x][y] = 9

        if f[x][y+1] == 1:
            if f[x+1][y] == 1:
                break
            x += 1
        else:
            y += 1
    elif f[x][y] == 2:
        f[x][y] = 9
        break

for i in range(len(f)):
    for j in range(len(f[0])):
        print(f[i][j], end=' ')
    print()

