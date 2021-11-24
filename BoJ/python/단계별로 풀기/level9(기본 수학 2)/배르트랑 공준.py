import sys
import math

def prime(num):
    if num == 0:
        return False

    else:
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                return False
        return True

prime_list = []

for i in range(2, 246912):
    if prime(i):
        prime_list.append(i)

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    result = 0
    for i in prime_list:
        if n < i and i <= n*2:
            result += 1
    print(result)