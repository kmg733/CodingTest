# https://www.acmicpc.net/problem/11664
import sys
input = sys.stdin.readline

Ax, Ay, Az, Bx, By, Bz, Cx, Cy, Cz = map(int, input().split())

answer = float('inf')
while True:
    Mx, My, Mz = (Ax + Bx) / 2, (Ay + By) / 2, (Az + Bz) / 2
    l = ((Ax - Cx) ** 2 + (Ay - Cy) ** 2 + (Az - Cz) ** 2) ** 0.5
    h = ((Mx - Cx) ** 2 + (My - Cy) ** 2 + (Mz - Cz) ** 2) ** 0.5
    r = ((Bx - Cx) ** 2 + (By - Cy) ** 2 + (Bz - Cz) ** 2) ** 0.5

    if abs(answer - h) <= 1e-6:
        print('0.1f'%answer)
        exit()
    if h < answer:
        answer = h
    if l > r:
        Ax, Ay, Az = Mx, My, Mz
    else:
        Bx, By, Bz = Mx, My, Mz