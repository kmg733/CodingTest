import sys

xList = []
yList = []

for i in range(3):
    x, y = map(int, sys.stdin.readline().split())
    xList.append(x)
    yList.append(y)

for i in range(3):
    if xList.count(xList[i]) == 1:
        targetX = xList[i]
    if yList.count(yList[i]) == 1:
        targetY = yList[i]

print(targetX, targetY)