m = int(input())
n = int(input())

sosu = []

for i in range(m, n+1):
    if i > 1:
        for j in range(2, i+1):
            if i == j:
                sosu.append(i)
            elif i % j == 0:
                break

if len(sosu) != 0:    
    print(sum(sosu))
    print(min(sosu))
else:
    print(-1)
