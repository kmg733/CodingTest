# https://www.acmicpc.net/problem/16198
import sys
input = sys.stdin.readline

def energy(e):
    # 재귀 사용하기 위해 전역 변수 선언
    global maxE, ary
    # ary 크기가 2라면 에너지 크기 비교후 현재 재귀 함수 리턴
    if len(ary) == 2:
        if maxE < e:
            maxE = e
        return
    else:
        for i in range(1, len(ary)-1):
            tempE = ary[i-1] * ary[i+1]
            temp = ary[i]
            del ary[i]
            energy(e+tempE)
            # 재귀 종료후 삭제했던 값 추가
            ary.insert(i, temp)
n = int(input())
ary = list(map(int, input().split()))
maxE = 0
energy(0)
print(maxE)

# 참고 : https://dongsik93.github.io/algorithm/2019/11/30/algorithm-boj-16198/