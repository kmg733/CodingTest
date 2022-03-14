# https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3

def solution(s):
    if len(s) == 1:
        return 1
    result = len(s)
    for cutLen in range(1, len(s) // 2 + 1):
        strs = ""
        temp = s[:cutLen]
        count = 1
        for i in range(cutLen, len(s), cutLen):
            # 같은 문자가 나온 경우
            if s[i:i + cutLen] == temp:
                count += 1
            # 다른 문자가 나온 경우
            else:
                # 직전의 문자가 한번만 나온 경우
                if count == 1:
                    strs += temp
                # 직전의 문자가 여러번 나온 경우
                else:
                    strs += str(count) + temp
                temp = s[i:i + cutLen]
                count = 1
        
        # 마지막 문자를 위해 한번더 처리
        # 직전의 문자가 한번만 나온 경우
        if count == 1:
            strs += temp
        # 직전의 문자가 여러번 나온 경우
        else:
            strs += str(count) + temp
        result = min(result, len(strs))
        
    return result