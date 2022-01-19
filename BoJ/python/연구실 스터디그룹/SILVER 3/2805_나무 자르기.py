# https://www.acmicpc.net/problem/2805
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
trees = sorted(map(int, input().split()))

# 자르고 가져가는 나무의 길이
def checkTreeLen(h):
    sum = 0
    for tree in trees:
        if tree > h:
            sum += (tree - h) 
    return sum

def binary(start, end):
    global m
    # start가 end보다 커지게 되면 end는 절단기 높이의 최대값을 가진다.
    if start > end:
        return end

    # 절단기의 높이
    mid = (start + end) // 2
    treeLen = checkTreeLen(mid)    

    if treeLen >= m:
        return binary(mid + 1, end)
    elif treeLen < m:
        return binary(start, mid - 1)

print(binary(1, trees[-1]))


# 이진 탐색