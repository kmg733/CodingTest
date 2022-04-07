# https://www.acmicpc.net/problem/1343
import sys
input = sys.stdin.readline

poli = input().strip()
poli = poli.replace('XXXX', 'AAAA')
poli = poli.replace('XX', 'BB')
if 'X' in poli:
    print(-1)
else:
    print(poli)