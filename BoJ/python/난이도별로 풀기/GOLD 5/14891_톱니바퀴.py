# https://www.acmicpc.net/problem/14891
from collections import deque 
import sys
input = sys.stdin.readline

# 2번 인덱스와 6번 인덱스가 맞닿아 있음
gear = [[]]
for i in range(1, 5):
    gear.append(deque(list(input().strip())))

def gearRight(start, direct):
    # 인덱스 범위를 넘어가면 회전 종료
    # 1 ~ 3까지만 체크, 4번째는 start + 1로 체크
    if start > 4:
        return

    # 2번 인덱스와 6번 인덱스가 같은 경우 회전 종료
    if gear[start - 1][2] == gear[start][6]:
        return

    # 2번 인덱스와 6번 인덱스가 다른 경우
    elif gear[start - 1][2] != gear[start][6]:
        gearRight(start + 1, -direct)
        gear[start].rotate(direct)


def gearLeft(start, direct):
    # 인덱스 범위를 넘어가면 회전 종료
    # 2 ~ 4까지만 체크, 1번째는 start - 1로 체크
    if start < 1:
        return

    # 2번 인덱스와 6번 인덱스가 같은 경우 회전 종료
    if gear[start + 1][6] == gear[start][2]:
        return

    # 2번 인덱스와 6번 인덱스가 다른 경우
    elif gear[start + 1][6] != gear[start][2]:
        gearLeft(start - 1, -direct)
        gear[start].rotate(direct)

# 회전 시키기 전에 회전 시킬 톱니 바퀴들을 먼저 확인 해야 모든 톱니바퀴의 회전여부를 알 수 있음 
# -> 재귀 통해서 처리하면 먼저 확인 안해도 됨
k = int(input())
for _ in range(k):
    gearNum, direction = map(int, input().split())

    # 선택한 톱니바퀴를 제외한 나머지 톱니바퀴 회전
    gearRight(gearNum + 1, -direction)
    gearLeft(gearNum - 1, -direction)
    
    # 마지막으로 선택한 톱니바퀴 회전
    gear[gearNum].rotate(direction)

result = 0
for i in range(1, 5):       
    # S극
    if gear[i][0] == '1':
        result += 2 ** (i - 1)
print(result)
