# https://www.acmicpc.net/problem/1072
import sys

X, Y = map(int, sys.stdin.readline().split())
Z = Y*100//X

# 히든케이스 2개
# 한번이라도 진 경우 승률 99에서 변하지 않음
# 승률 100이상은 올라가지 않음
if Z >= 99:
    print(-1)

# 시간초과 문제해결을 위해 이분탐색(logN) 이용
# 이분탐색 사용 질문: X+1 번의 탐색후에 정답이 구해진다면 이분탐색으로는 답을 못찾는것이 아닌가?

else:
    result = 0
    left = 1
    right = X

    while left <= right:
        mid = (left + right) // 2
        if (Y + mid) * 100 // (X + mid) <= Z:
            left = mid + 1
        else:
            right = mid - 1
            result = mid

    print(result)