# https://www.acmicpc.net/problem/1966
testCase = int(input())

for _ in range(testCase):
    n, m = map(int,input().split())

    printList = list(map(int,input().split()))
    checkList = [0 for _ in range(n)] 
    checkList[m] = 1

    count=0
    while True:
        # 큐안에 있는 가장 큰 값이라면
        if printList[0] == max(printList):
            count+=1

            # 찾는 값이 아니라면
            if checkList[0] != 1:
                del printList[0]
                del checkList[0]
            # 찾는 값이라면
            else:
                print(count)
                break
        
        # 그 외값은 큐의 마지막 순위에 추가
        else:
            printList.append(printList[0])
            checkList.append(checkList[0])
            del printList[0]
            del checkList[0]