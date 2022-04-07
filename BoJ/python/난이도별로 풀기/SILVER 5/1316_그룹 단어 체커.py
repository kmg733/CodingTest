# https://www.acmicpc.net/problem/1316
import sys

n = int(sys.stdin.readline().strip())
count = n

for i in range(n):
    w = str(sys.stdin.readline().strip())
    for j in range(len(w)-1):
        if w[j] != w[j+1]:
            testWord = w[j+1:]
            if w[j] in testWord:
                count -= 1
                break

print(count)