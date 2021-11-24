n, m = map(int, input().split())
numberList = list(map(int, input().split()))

big = 0

for i in range(len(numberList)):
    for j in range(i+1, len(numberList)):
        for k in range(j+1, len(numberList)):
            if big == m:
                break
            sum = numberList[i] + numberList[j] + numberList[k]
            if sum <= m:
                if sum > big:
                    big = sum

print(big)