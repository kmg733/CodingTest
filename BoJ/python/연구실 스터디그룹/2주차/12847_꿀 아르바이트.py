import sys
input = sys.stdin.readline

n, m = map(int, input().split())
t = list(map(int, input().split()))

hap = sum(t[:m])
result = hap
for i in range(m, n):
    hap += t[i] - t[i - m]
    result = max(result, hap)

print(result)
# 시간초과 - for문 안에 list append와 sum 연산자를 같이 사용해서 그런것 같음
# n, m = map(int, input().split())
# t = list(map(int, input().split()))

# hap = []
# for i in range(n - (m - 1)):
#     hap.append(sum(t[i:m+i]))

# print(max(hap))