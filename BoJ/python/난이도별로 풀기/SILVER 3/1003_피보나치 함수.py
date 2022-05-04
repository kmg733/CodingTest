# https://www.acmicpc.net/problem/1003
import sys
input = sys.stdin.readline

# 0일때 1번, 1일때 0번, 2일때 1번
zero = [1, 0, 1]
# 0일때 0번, 1일때 1번, 2일때 1번
one = [0, 1, 1]

# 피보나치 n에서 0, 1의 호출 횟수는 
# n - 1과 n - 2에서 0, 1을 호출한 횟수를 더한것과 같음 
# -> fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)
def fibonacci(num):
    length = len(zero)
    if num >= length:
        for i in range(length, num + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print(f"{zero[num]} {one[num]}")

t = int(input())
    
for _ in range(t):
    fibonacci(int(input()))