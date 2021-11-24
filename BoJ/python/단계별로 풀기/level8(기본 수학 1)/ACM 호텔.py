t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    if n % h == 0:
        room = n // h
        floor = h
    else:
        room = n // h + 1
        floor = n % h
    print(floor * 100 + room)