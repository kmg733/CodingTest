t = int(input())

for i in range(t):
    floor = int(input())
    room = int(input())
    floor0 = list(range(1, room+1))
    
    for j in range(floor):
        for k in range(1, room):
            floor0[k] += floor0[k-1]
    print(floor0[-1])