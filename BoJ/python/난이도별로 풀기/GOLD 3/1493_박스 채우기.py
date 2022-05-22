# https://www.acmicpc.net/problem/1493

import sys
input = sys.stdin.readline

l, w, h = map(int, input().split())
n = int(input())
cube = []
for _ in range(n):
    cube.append(list(map(int, input().split())))
cube.sort(reverse = True)

volume = l * w * h
answer = 0
# 채워진 큐브의 넓이
# 큰것부터 역순으로 (큐브 개수 * 2 ** 3) * 큐브 개수 * 2 ** 3
before = 0
for side, each in cube:
    # 각 변마다 2제곱씩 증가하므로 세 변을 합쳐 총 2 ** 3(8배)씩 증가한다
    # 1 * 1 * 1 -> 2 * 2 * 2 -> 4 * 4 * 4 
    before *= 2 ** 3
    sideLen = 2 ** side

    # 박스에 들어갈 수 있는 큐브의 최대 갯수
    # 박스에 채워진 공간만큼 뺌(before) 
    maxCount = (l // sideLen) * (w // sideLen) * (h // sideLen) - before
    # 수량 제한이 있으므로 확인
    maxCount = min(each, maxCount)
    answer += maxCount    
    before += maxCount

if volume == before:
    print(answer)
else:
    print(-1)