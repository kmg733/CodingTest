n = set(range(1, 10001))
removeN = set()

for i in range(1, 10001):   # i = 850
    for j in str(i):        # j = "8", "5", "0"
        i += int(j)         # 850 + 8 + 5 + 0, i = 863
    removeN.add(i)          

selfNum = sorted(n - removeN)
for i in selfNum:
    print(i)

#참고:https://wook-2124.tistory.com/252