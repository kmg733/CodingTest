a, b = map(int, input().split())
a = bool(a)
b = bool(b)
if ((a and not b) or (not a and b)):
    print(True)
else:
    print(False)