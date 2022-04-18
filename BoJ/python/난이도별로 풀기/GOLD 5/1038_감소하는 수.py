# https://www.acmicpc.net/problem/1038
import sys
input = sys.stdin.readline

# 백 트래킹을 재귀적으로 구현
def backTrack(digit, num):
    # 자릿수가 한자리 라면 무조건 감소하는 수
    if digit == 1:
        d.append(num)
    else:
        # 다음에 붙일 숫자는, 앞의 숫자보다 작아야 하므로
        # num % 10으로 앞 자리의 수를 구하고 for문 수행
        for i in range(num % 10):
            backTrack(digit - 1, num * 10 + i)

# 감소하는 숫자 리스트
d = []
# 문제를 만족하는 가장 큰 숫자는 9,876,543,210이다.
# 때문에 10자릿수까지만 검사하면 되므로, for문 범위는 1 ~ 10까지
for i in range(1, 11):
    # 검사할 숫자 0 ~ 9까지
    for j in range(i - 1, 10):
        backTrack(i, j)

n = int(input())
if len(d) <= n:
    print(-1)
else:
    print(d[n])

# 참고: https://khsung0.tistory.com/22