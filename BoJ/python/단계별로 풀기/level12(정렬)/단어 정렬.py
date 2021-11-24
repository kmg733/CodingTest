import sys

n = int(input())
strs = []

for _ in range(n):
    strs.append(sys.stdin.readline().strip())

strs = list(set(strs))
strs.sort()
strs.sort(key = lambda x:len(x))

for i in range(len(strs)):
    print(strs[i])
   
# sort 사용법 참고: https://kingofbackend.tistory.com/98 