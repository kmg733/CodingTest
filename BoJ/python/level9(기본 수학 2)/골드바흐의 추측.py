import sys
import math

def prime(num):
    if num == 0:
        return False
    
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    left = int(n/2)
    right = int(n/2)

    for i in range(int(n/2)):
        if prime(left) == True and prime(right) == True:
            print(left, right)
            break
        else:
            left -= 1
            right += 1

            