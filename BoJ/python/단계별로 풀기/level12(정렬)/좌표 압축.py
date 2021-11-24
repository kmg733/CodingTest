import sys

n = int(input())
lists = list(map(int, sys.stdin.readline().split()))
rank = sorted(list(set(lists)))
dic = {}

for i in range(len(rank)):
    dic[rank[i]] = i

for i in range(n):
    lists[i] = dic[lists[i]]
    print(lists[i], end=' ')
