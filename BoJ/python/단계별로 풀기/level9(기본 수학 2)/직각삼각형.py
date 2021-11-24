import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())

    if a == 0 and b == 0 and c == 0:
        break

    biggest = max(a, b, c)

    if a == biggest:
        if c**2 + b**2 == a**2:
            print('right')
        else:
            print('wrong')

    elif b == biggest:
        if a**2 + c**2 == b**2:
            print('right')
        else:
            print('wrong')

    else:
        if a**2 + b**2 == c**2:
            print('right')
        else:
            print('wrong')