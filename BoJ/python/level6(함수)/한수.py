# 문제 해석
# 123의 숫자가 있다고 하면 자릿수대로 이 숫자들을 하나씩 분리한다.
# 그럼 1, 2, 3의 숫자가 된다. 이 숫자들은 등차수열을 이루므로 123은 한수이다.
# 주의할 것은 1부터 9까지도 한수에 포함한다.

import sys

n = int(sys.stdin.readline())
hansu = 0

for i in range(1, n+1):
    if i < 100:
        hansu += 1
    else:
        temp = list(map(int, str(i)))
        if temp[0] - temp[1] == temp[1] - temp[2]:
            hansu += 1
        
print(hansu)