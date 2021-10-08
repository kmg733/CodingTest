n = int(input())

strs = list(str(n))
strs.sort(reverse=True)

print(''.join(strs))