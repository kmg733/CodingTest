import sys

a = []
for i in range(10):
    a.append(int(sys.stdin.readline()) % 42)

# 중복 제거 list(set(리스트))
a = list(set(a))
print(len(a))
