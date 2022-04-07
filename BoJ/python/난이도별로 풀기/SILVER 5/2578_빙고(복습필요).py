# https://www.acmicpc.net/problem/2578
import sys

# dict로 참가자 빙고판 인덱스 기록
plate = dict()
for i in range(5):
    a = list(map(int, sys.stdin.readline().split()))
    for j in range(5):
        plate[a[j]] = [i, j]

# 사회자 빙고판
stack = 0
moderator = []
chk = [[0]*5 for i in range(5)]
for i in range(5):
    moderator.append(list(map(int, sys.stdin.readline().split())))

for i in range(5):
    for j in range(5):
        chk[plate[moderator[i][j]][0]][plate[moderator[i][j]][1]] = 1

        stack += 1
        bingoCount = 0
        
        for k in range(5):
            # 가로빙고 확인
            if sum(chk[k]) == 5:
                bingoCount += 1        

            # 세로빙고 확인
            s = 0
            # if sum([l[k] for l in chk]) == 5:
            for l in range(5):
                if chk[l][k] == 1:
                    s += 1
                if s == 5:
                    bingoCount += 1

        # 대각선빙고 확인
        if chk[0][4] + chk[1][3] + chk[2][2] + chk[3][1] + chk[4][0] == 5:
            bingoCount += 1
        if chk[0][0] + chk[1][1] + chk[2][2] + chk[3][3] + chk[4][4] == 5:
            bingoCount += 1
        
        if bingoCount >= 3:
            print(stack)
            sys.exit()

# 참고 : https://my-coding-notes.tistory.com/236