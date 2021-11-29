# https://www.acmicpc.net/problem/1914
import sys

def hanoi(n, bFrom, bTo, other):
    if n == 0:
        return
    
    hanoi(n-1, bFrom, other, bTo)
    move.append([bFrom, bTo])
    hanoi(n-1, other, bTo, bFrom)

n = int(sys.stdin.readline())
move = []

if n <= 20:
    hanoi(n, 1, 3, 2)
    print(len(move))
    for i in range(len(move)):
        print(move[i][0], move[i][1])
else:
    print(2 ** n - 1)



# 풀이참고 : https://www.youtube.com/watch?v=aPYE0anPZqI
# 풀이참고2 : https://data-jj.tistory.com/34
# 풀이참고3 : https://bgspro.tistory.com/6