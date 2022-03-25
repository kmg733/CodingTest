# https://www.acmicpc.net/problem/3041
import sys
input = sys.stdin.readline

result = 0
for i in range(4):
    puzzle = list(input().strip())
    for j in range(4):
        if puzzle[j] != '.':
            # 행 차이 계산
            result += abs((ord(puzzle[j]) - ord('A')) // 4 - i)
            # 열 차이 계산
            result += abs((ord(puzzle[j]) - ord('A')) % 4 - j)

print(result)