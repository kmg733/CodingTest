# 소수인지 판단하는 것은 해당 값의 제곱근 까지만 확인하면 된다.

import sys
import math

m, n = map(int, sys.stdin.readline().split())

for i in range(m, n+1):
    if i == 1:
        pass
    else:
        sosu = True
        sqrt = int(math.sqrt(i))

        for j in range(2, sqrt+1):
            if i % j == 0:
                sosu = False
                break
        
        if sosu == True:
            print(i)