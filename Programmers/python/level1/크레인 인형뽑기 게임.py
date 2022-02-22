# https://programmers.co.kr/learn/courses/30/lessons/64061
from collections import deque

def solution(board, moves):
    answer = 0
    stack = deque()
    for move in moves:
        for i in range(len(board)):
            value = board[i][move - 1]
            if value != 0:
                if len(stack) > 0:
                    # 그 전에 넣은 인형과 마지막에 넣은 인형이 같은경우
                    if stack[-1] == value:
                        answer += 2
                        stack.pop()
                    else:
                        stack.append(value)
                else:
                    stack.append(value)
                board[i][move - 1] = 0
                break

    return answer

# 다른 사람의 풀이
# def solution(board, moves):
#     stacklist = []
#     answer = 0

#     for i in moves:
#         for j in range(len(board)):
#             if board[j][i-1] != 0:
#                 stacklist.append(board[j][i-1])
#                 board[j][i-1] = 0

#                 if len(stacklist) > 1:
#                     if stacklist[-1] == stacklist[-2]:
#                         stacklist.pop(-1)
#                         stacklist.pop(-1)
#                         answer += 2     
#                 break

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))

# 파이썬 deque의 peek : https://stackoverflow.com/questions/48640251/how-to-peek-front-of-deque-without-popping


# 파이썬 List의 pop은 O(1)의 시간복잡도를 가지므로, 
# 내가 풀이에 사용한 deque를 사용하지 않고 List의 pop을 사용해도 상관없다.
# deque를 사용할 경우는 popleft를 사용해야할 경우이다.