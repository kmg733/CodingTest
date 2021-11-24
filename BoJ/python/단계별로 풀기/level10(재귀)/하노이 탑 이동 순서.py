def hanoi(n, bFrom, bTo, other):        # 각 매개변수는 원판개수, 시작기둥, 목표기둥, 보조기둥을 의미함
    if n == 0:
        return

    hanoi(n - 1, bFrom, other, bTo)     # 남은 원반 중 가장 큰 원반을 제외하고 모두 보조기둥으로 이동시킴
    movement.append([bFrom, bTo])   
    hanoi(n - 1, other, bTo, bFrom)     # 가장 큰 원반을 목표기둥으로 이동

t = int(input())
movement = []
hanoi(t, 1, 3, 2)
print(len(movement))

for i in range(len(movement)):
    print(movement[i][0], movement[i][1])

#참고: https://data-jj.tistory.com/34