# https://www.acmicpc.net/problem/5904
import sys
input = sys.stdin.readline

def moo(n, k, l):
    if n <= 3:
        if n == 1:
            return 'm'
        else:
            return 'o'

    new_l = l * 2 + k + 3
    if n > new_l:
        return moo(n, k+1, new_l)
    else:
        if n > l and n <= l + k + 3:
            if n - l == 1:
                return 'm'
            else:
                return 'o'
        else:
            return moo(n-(l+k+3), 1, 3)

n = int(input())
print(moo(n, 1, 3))

#참고: https://d-cron.tistory.com/18