n = int(input())
count = n

for i in range(n):
    w = input()
    for j in range(len(w)-1):
        if w[j] != w[j+1]:
            testWord = w[j+1:]
            if w[j] in testWord:
                count -= 1
                break

print(count)