# https://www.acmicpc.net/problem/1105
import sys
input = sys.stdin.readline
l, r = map(str, input().split())

# 두 숫자의 길이가 같은경우와 다른경우로 규칙을 찾을 수 있음
count = 0
# 두 숫자의 길이가 다르면 8을 하나도 포함하지 않는 숫자가 존해하므로 0출력
if len(l) != len(r):
    print(0)
# 두 숫자의 길이가 같은경우
else:
    for i in range(len(l)):
        # 같은 자릿수에 8이 존재하면 무조껀 8이 포함되므로 +1
        if l[i] == r[i]:
            if l[i] == '8':
                count += 1
        else:
            break
    print(count)

# 그리디 알고리즘