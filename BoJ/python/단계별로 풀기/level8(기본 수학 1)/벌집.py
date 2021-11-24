a = int(input())

path = 1
plus = 1

while a > plus:
    plus += 6 * path
    path += 1

print(path)