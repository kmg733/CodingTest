import sys

t = int(sys.stdin.readline())

for i in range(t):
    result = ''
    count, str = sys.stdin.readline().split()
    for j in range(len(str)):
        result += str[j]*int(count)
    print(result)

# 숏코딩

# for i in range(t):
#     count, str = sys.stdin.readline().split()
#     for j in str:
#         print(j*int(count), end="")
#     print()