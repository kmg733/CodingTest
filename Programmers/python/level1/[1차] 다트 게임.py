# https://programmers.co.kr/learn/courses/30/lessons/17682
def solution(dartResult):
    answer = []
    nums = [str(x) for x in range(11)]
    chars = ['S', 'D', 'T']
    startSharp = ['*', '#']
    
    startIdx = 0  
    endIdx = -1
    for idx, d in enumerate(dartResult):
        if d in chars:
            # 끝 인덱스인 경우
            if idx + 1 == len(dartResult):
                endIdx = idx
            else:
                # 스타상이나 아차상이 들어있는 경우
                if dartResult[idx + 1] in startSharp:
                    endIdx = idx + 1
                else:
                    endIdx = idx

            num = int(dartResult[startIdx : idx])

            # S인경우 아무것도 안해도 됨
            if d == 'D':
                num = num ** 2
            elif d == 'T':
                num = num ** 3
            
            if dartResult[endIdx] == '*':
                if len(answer) > 0:
                    answer[-1] = answer[-1] * 2
                answer.append(num * 2)
            elif dartResult[endIdx] == '#':
                answer.append(-num)
            else:
                answer.append(num)
            startIdx = endIdx + 1
    return sum(answer)

dartResult = '1S*2T*3S'
print(solution(dartResult))