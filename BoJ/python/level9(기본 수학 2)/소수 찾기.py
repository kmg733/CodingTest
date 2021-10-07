n = int(input())
b = list(map(int, input().split()))

count = 0

for i in b:
    stack = 2
    while i >= stack:        
        if i == stack:
            count += 1
            break
        elif i % stack == 0:
            break
        stack += 1

print(count)