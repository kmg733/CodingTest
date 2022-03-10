# https://www.acmicpc.net/problem/14503
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
startX, startY, startD = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

visited = [[0] * m for _ in range(n)]
# 북, 동, 남, 서 순서임
dxy = [[-1, 0], [0, 1], [1, 0], [0, -1]]

count = 1
visited[startX][startY] = 1
while True:
    flag = False
    for _ in range(4):
        # 바라보는 방향의 왼쪽 방향 좌표 구하기
        newX = startX + dxy[(startD + 3) % 4][0]
        newY = startY + dxy[(startD + 3) % 4][1]
        startD = (startD + 3) % 4

        if 0 <= newX < n and 0 <= newY < m and graph[newX][newY] == 0:
            if visited[newX][newY] == 0:
                visited[newX][newY] = 1
                count += 1
                startX = newX
                startY = newY
                flag = True
                break
                
    if flag == False:
        # 후진했을 때 벽인경우
        if graph[startX - dxy[startD][0]][startY - dxy[startD][1]] == 1:
            print(count)
            break
        else:
            startX -= dxy[startD][0]
            startY -= dxy[startD][1] 

# 구현
# DFS/BFS와 유사함