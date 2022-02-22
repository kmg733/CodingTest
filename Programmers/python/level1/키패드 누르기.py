# https://programmers.co.kr/learn/courses/30/lessons/67256

from dis import dis


def solution(numbers, hand):
    answer = []
    keyPad = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '*', '0', '#']    
    startL = '*'
    startR = '#'
    for num in numbers:
        destination = str(num)
        if destination in ['1', '4', '7', '*']:
            answer.append('L')
            startL = destination
        elif destination in ['3', '6', '9', '#']:
            answer.append('R')
            startR = destination
        else:
            l = keyPad.index(startL)
            r = keyPad.index(startR)
            d = keyPad.index(destination)
            distanceL =  abs(l // 3 - d // 3) + abs(l % 3 - d % 3)
            distanceR =  abs(r // 3 - d // 3) + abs(r % 3 - d % 3)
            print(f"{destination} {distanceL} {distanceR}")
            if distanceL < distanceR:
                answer.append('L')
                startL = destination
            elif distanceL > distanceR:
                answer.append('R')
                startR = destination
            else:
                if hand == 'left':
                    answer.append('L')
                    startL = destination
                else:
                    answer.append('R')
                    startR = destination

    return ''.join(answer)

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))