# https://programmers.co.kr/learn/courses/30/lessons/77485
# 리스트의 깊은 복사와 얕은 복사에 대해서 알아보기
import copy

def solution(rows, columns, queries):
    answer = []    
    graph = [[i + (columns * j) for i in range(1, columns + 1)] for j in range(rows)]

    for x1, y1, x2, y2 in queries:
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        temp = graph[x1][y1]
        minNum = temp
        
        # 왼쪽
        for x in range(x1, x2):
            temp2 = graph[x + 1][y1]
            graph[x][y1] = temp2
            minNum = min(minNum, temp2)
        
        # 아래
        for y in range(y1, y2):
            temp2 = graph[x2][y + 1]
            graph[x2][y] = temp2
            minNum = min(minNum, temp2)
               
        # 오른쪽
        for x in range(x2, x1, -1):
            temp2 = graph[x - 1][y2]
            graph[x][y2] = temp2
            minNum = min(minNum, temp2)
        
        # 위
        for y in range(y2, y1, -1):
            temp2 = graph[x1][y - 1]
            graph[x1][y] = temp2
            minNum = min(minNum, temp2)
        
        graph[x1][y1 + 1] = temp
        answer.append(minNum)
    
    return answer

# 시간초과된 문제풀이
def solution2(rows, columns, queries):
    answer = []
    
    graph = [[i + (columns * j) for i in range(1, columns + 1)] for j in range(rows)]
    newGraph = copy.deepcopy(graph)
    for x1, y1, x2, y2 in queries:
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        nums = []
        for i in range(1, abs(y1 - y2) + 1):
            newGraph[x1][y1 + i] = graph[x1][y1 + i - 1]
            nums.append(newGraph[x1][y1 + i])

        for i in range(1, abs(x1 - x2) + 1):
            newGraph[x1 + i][y2] = graph[x1 + i - 1][y2]
            nums.append(newGraph[x1 + i][y2])
        
        for i in range(1, abs(y1 - y2) + 1):
            newGraph[x2][y2 - i] = graph[x2][y2 - i + 1]
            nums.append(newGraph[x2][y2 - i])

        for i in range(1, abs(x1 - x2) + 1):
            newGraph[x2 - i][y1] = graph[x2 - i + 1][y1]
            nums.append(newGraph[x2 - i][y1])
        
        answer.append(min(nums))
        graph = copy.deepcopy(newGraph)
            
    return answer

# 참고(깊은 복사와 얕은 복사): https://black-hair.tistory.com/49
