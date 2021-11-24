s = input()

chg = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in chg:
    s = s.replace(i, '*')
print(len(s))