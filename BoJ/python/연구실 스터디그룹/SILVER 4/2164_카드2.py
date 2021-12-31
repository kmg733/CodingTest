# https://www.acmicpc.net/problem/2164
# 큐와 관련된 문제임
# 시간 복잡도가 O(1)인 deque 라이브러리를 사용할것
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
card = deque()

for i in range(n, 0, -1):
    card.append(i)

while len(card) > 1:
    card.pop()
    card.rotate(1)

print(card.pop())
# 참고: https://leonkong.cc/posts/python-deque.html
