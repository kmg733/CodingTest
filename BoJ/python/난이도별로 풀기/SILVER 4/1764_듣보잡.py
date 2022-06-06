# https://www.acmicpc.net/problem/1764
n , m = map(int,input().split())
str1 = set()
str2 = set()

for _ in range(n):
    str1.add(input())
for _ in range(m):
    str2.add(input())

arr = sorted(list(str1 & str2))
print(len(arr))

for i in arr:
    print(i)