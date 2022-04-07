# https://www.acmicpc.net/problem/5107
from collections import deque
import sys
input = sys.stdin.readline

def bfs(j):
    global answer
    answer += 1
    que = deque()
    que.append(j)

    while que:
        a = que.popleft()
        for i in range(n):
            if graph[a][i] == 1:
                que.append(i)
                graph[a][i] = 0
                graph[i][a] = 0
    

count = 1
while True:
    n = int(input())
    if n == 0:
        break        
    
    chain = []
    chainIndex = dict()
    for i in range(n):
        a, b = input().split()  
        chain.append([a, b])
        chainIndex[a] = i

    visited = [False] * n
    graph = [[0] * n for _ in range(n)]
    for i in range(n):
        graph[chainIndex[chain[i][0]]][chainIndex[chain[i][1]]] = 1
        graph[chainIndex[chain[i][1]]][chainIndex[chain[i][0]]] = 1
    
    answer = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 or graph[j][i] == 1:
                graph[i][j] = 0
                graph[j][i] = 0                
                bfs(j)
    print(count, answer)
    count += 1
# def soloution(x):
#     visited[x] = 1
#     global count

#     for i in range(n):
#         if mpa[x][i] == 1:
#             if visited[i] == 0:
#                 soloution(i)
#             else:
#                 count += 1
#             break
#     return 

# t = 1
# while True:
#     n = int(input())
#     if n == 0:
#         break
    
#     count = 0
#     chain = []
#     chainIndex = dict()
#     for i in range(n):
#         a, b = input().split()  
#         chain.append([a, b])    
#         chainIndex[a] = i

#     visited = [0] * n
#     mpa = [[0] * n for _ in range(n)]
#     for i in range(len(chain)):
#         mpa[chainIndex[chain[i][0]]][chainIndex[chain[i][1]]] = 1

#     for i in range(n):
#         if visited[i] == 0:
#             for j in range(n):
#                 if mpa[i][j] == 1 and visited[j] == 0:
#                     visited[i] = 1
#                     soloution(j)
    
#     print(t, count)
#     t += 1
# ===========================
# answer = 0
# count = 1


# def bfs(g):
#     global answer
#     answer = 0
#     for i in range(n):
#         for j in range(n):
#             if g[i][j] == 1:
#                 g[i][j] = 0
#                 g[j][i] = 0
#                 que = [j]
#                 answer += 1
#                 while que:
#                     haha = que.pop(0)
#                     for k in range(n):
#                         if g[haha][k] == 1:
#                             que.append(k)
#                             g[haha][k] = 0
#                             g[k][haha] = 0


# while True:
#     n = int(input())
#     if n == 0:
#         break
#     graph = [[0] * n for _ in range(n)]
#     people = []
#     for _ in range(n):
#         f1 = False
#         f2 = False
#         name1, name2 = input().split()
#         if name1 not in people:
#             people.append(name1)
#             f1 = True
#         if name2 not in people:
#             people.append(name2)
#             f2 = True

#         if f1 and f2:
#             graph[len(people) - 1][len(people) - 2] = 1
#             graph[len(people) - 2][len(people) - 1] = 1
#         else:
#             index1 = 0
#             index2 = 0
#             for i in range(len(people)):
#                 if people[i] == name1:
#                     index1 = i
#                 if people[i] == name2:
#                     index2 = i
#             graph[index1][index2] = 1
#             graph[index2][index1] = 1
#     bfs(graph)
#     print(count, answer)
#     count += 1 