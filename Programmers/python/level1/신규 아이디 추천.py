# https://programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    word = [chr(c) for c in range(ord('a'), ord('z') + 1)]
    word2 = [chr(c) for c in range(ord('0'), ord('9')+1)]
    word.extend(['-', '_', '.'])
    word.extend(word2)

    # 2단계
    for c in new_id:
        if c not in word:
            new_id = new_id.replace(c, "")
            
    # 3단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    # 4단계
    new_id = new_id.strip('.')

    # 5단계
    if len(new_id) == 0:
        new_id = 'a'

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[0:15].strip('.')
    
    # 7단계
    if len(new_id) <= 2:
        while(len(new_id) < 3):
            new_id = new_id + new_id[-1]
    return new_id

# 다른 사람의 풀이
# import re

# def solution(new_id):
#     st = new_id
#     st = st.lower()
#     st = re.sub('[^a-z0-9\-_.]', '', st)
#     st = re.sub('\.+', '.', st)
#     st = re.sub('^[.]|[.]$', '', st)
#     st = 'a' if len(st) == 0 else st[:15]
#     st = re.sub('^[.]|[.]$', '', st)
#     st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
#     return st

new_id = "...!@BaT#*..y.abcdefghijklm"
print(solution(new_id))

