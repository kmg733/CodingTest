n = int(input())
a = map(int ,input().split())
s = 10000

for i in a:
    if s > i:
        s = i

print(s)