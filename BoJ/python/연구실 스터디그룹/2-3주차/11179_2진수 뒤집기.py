# https://www.acmicpc.net/problem/11179
import sys

n = int(sys.stdin.readline())
b = list(bin(n))[2:]
print(int("".join(reversed(b)), 2))

# n = int(sys.stdin.readline())
# b = list(bin(n))
# d = ['0', 'b']
# for i in list(reversed(b[2:])):
#     d.append(i)
# print(int("".join(d), 2))

