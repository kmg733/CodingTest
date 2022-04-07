# https://www.acmicpc.net/problem/3584
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    # 각 노드의 부모를 저장할 리스트
    graph = [0] * (n + 1)

    # graph 리스트의 인덱스(자식)에 부모 노드를 저장
    for _ in range(n - 1):
        parentNode, childNode = map(int, input().split())
        graph[childNode] = parentNode

    a, b = map(int, input().split())

    aParentList = [a]
    bParentList = [b]

    # a의 부모들을 aParentList에 저장
    while graph[a]:
        aParentList.append(graph[a])
        a = graph[a]

    # b의 부모들을 bParentList에 저장
    while graph[b]:
        bParentList.append(graph[b])
        b = graph[b]
    
    # 맨 위층에서부터 부모 노드가 달라질 때를 찾음
    aIdx = len(aParentList) - 1
    bIdx = len(bParentList) - 1
    while aParentList[aIdx] == bParentList[bIdx]:
        aIdx -= 1
        bIdx -= 1
    
    print(aParentList[aIdx + 1])

# 참고: https://fre2-dom.tistory.com/236
# 최소 공통 조상