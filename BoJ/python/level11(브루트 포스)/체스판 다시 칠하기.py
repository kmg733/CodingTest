import sys

n, m = map(int, sys.stdin.readline().split())
plate = []
result = []

for _ in range(n):
    plate.append(sys.stdin.readline())

for i in range(n - 7):          # n이 9이상일 경우를 확인하기 위해
    for j in range(m - 7):      # m이 9이상일 경우를 확인하기 위해
        startWhite = 0
        startBlack = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if plate[k][l] != 'W':
                        startWhite += 1
                    if plate[k][l] != 'B':
                        startBlack += 1
                else:
                    if plate[k][l] != 'B':
                        startWhite += 1
                    if plate[k][l] != 'W':
                        startBlack += 1
        result.append(startWhite)
        result.append(startBlack)

print(min(result))