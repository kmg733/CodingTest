a, b = map(int, input().split())
a = bool(a)
b = bool(b)
if (not a and not b) or (a and b):
    print(True)
else:
    print(False)
