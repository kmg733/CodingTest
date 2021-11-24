a, b = input().split()
a = int(a)
b = int(b)

if b < 45:
    if a > 0:
        print(a-1, b-45+60)
    else:
        print(23, b-45+60)
else:
    print(a, b-45)
