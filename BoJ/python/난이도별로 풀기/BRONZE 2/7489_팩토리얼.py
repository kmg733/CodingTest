import sys

def facto(n):
    x = 1
    for i in range(1, n+1):
        x *= i
    return x

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    s = list(str(facto(n)))
    while(True):
        if s[-1] == '0':
            del s[-1]
        else:
            print(s[-1])
            break
