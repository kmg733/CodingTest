import sys

# for문을 사용하여 입력받을 때에는 input()대신 sys.stdin.readline()를 사용하자.
# 문자열일 경우 .rstrip()까지 추가
# 참고1: https://www.acmicpc.net/board/view/22716
# 참고2: https://www.acmicpc.net/problem/15552
T = input()
T = int(T)
for i in range(T):
    a, b = sys.stdin.readline().split()
    a = int(a)
    b = int(b)
    print(a+b)