n = int(input())

soin = 2
result = []

while True:
    if n == 1:
        break
    elif n % soin == 0:
        result.append(soin)
        n = n / soin
    else:
        soin += 1
    
for i in result:
    print(i)