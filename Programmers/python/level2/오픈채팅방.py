# https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3
def solution(record):
    answer = []
    # 최종적으로 저장될 이름만 dic 변수에 저장한다.
    dic = {}
    # Enter와 Change의 경우만 닉네임이 바뀌기 때문에 해당의 경우만 확인하면 된다.
    for r in record:
        strs = r.split()
        if len(strs) == 3:
            dic[strs[1]] = strs[2]
            
    for r in record:
        strs = r.split()
        if strs[0] == 'Enter':
            answer.append(dic[strs[1]] + '님이 들어왔습니다.')
        elif strs[0] == 'Leave':
            answer.append(dic[strs[1]] + '님이 나갔습니다.')
    return answer