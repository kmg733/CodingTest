import sys

n = int(sys.stdin.readline())
info = []

for _ in range(n):
    info.append(list(map(int, sys.stdin.readline().split())))


for i in info:
    rank = 1

    for j in info:
        if i == j:
            pass
        
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")    
