# https://www.acmicpc.net/problem/1068
import sys
input = sys.stdin.readline

def dfs(dels, ary):
    ary[dels] = -2
    for i in range(len(ary)):
        # 삭제한 노드를 부모노드로 가지고 있는 수 삭제(리스트의 값 = 자신의 부모 노드) 
        if dels == ary[i]:
            dfs(i, ary)

n = int(input())
ary = list(map(int, input().split()))
delNode = int(input())
count = 0

# 삭제
dfs(delNode, ary)
# 리프노드 개수세기
for i in range(len(ary)):
    if ary[i] != -2 and i not in ary:
        count += 1
print(count)