# https://www.acmicpc.net/problem/1107
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
# 고장난 버튼이 있는 경우
if m:
    b = list(map(int, input().split()))
# 고장난 버튼이 없는 경우
else:
    b = []

# 초기 값은 최대 값으로, + 또는 -만 사용하는 경우 
answer = abs(100 - n)
# 완전 탐색
# 이동하려고 하는 채널의 범위가 0 <= N <= 500,000 이므로
# 500,000의 경우 1,000,000번 채널에서부터 내려오는 경우도 있으므로 1,000,000까지 탐색
for num in range(1000001):
    for c in str(num):
        # 번호를 눌러 해당 숫자를 만들 수 없을 경우
        if int(c) in b:
            break

    # 번호를 눌러 해당 숫자를 만들 수 있다면
    else:
        # min(이전 값, 번호를 누른 횟수 + 목표 값과의 차이[+ 또는 -를 누르는 횟수])
        answer = min(answer, len(str(num)) + abs(num - n))

print(answer)