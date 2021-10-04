import sys 

a = []
for i in range(9):
    a.append(int(sys.stdin.readline()))
    
m = max(a)
idx = a.index(m)
print(m)
print(idx+1)

