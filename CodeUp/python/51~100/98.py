a = []
for i in range(10):
    a.append(input().split())
    a[i] = list(map(int, a[i]))

x = int(1)
y = int(1)
while True:
    a[x][y] = 9
    if a[x][y+1] == 0:
        y += 1
    elif a[x][y+1] == 1:
        if a[x+1][y] == 0:
            x += 1
        elif a[x+1][y] == 1:
            break
        else:
            a[x+1][y] = 9
            break
    else:
        a[x][y+1] = 9
        break

for i in range(10):
    for j in range(10):
        print(a[i][j], end=' ')
    print()
