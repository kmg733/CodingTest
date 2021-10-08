n = int(input())

for i in range(1, n+1):
    if i == n:
        print(0)
        break

    numberList = map(int, str(i))
    hap = sum(numberList) + i

    if hap == n:
        print(i)
        break
    
