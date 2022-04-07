# https://www.acmicpc.net/problem/2954
import sys

s = str(sys.stdin.readline())
s = s.replace('apa', 'a')
s = s.replace('epe', 'e')
s = s.replace('ipi', 'i')
s = s.replace('opo', 'o')
s = s.replace('upu', 'u')
print(s)