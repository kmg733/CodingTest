# https://programmers.co.kr/learn/courses/30/lessons/12926
def solution(s, n):
    answer = ''
    for a in s:
        # 알파벳?
        if a.isalpha():
            # 소문자?
            if a.islower():
                if ord(a) + n > ord('z'):
                    answer += chr(ord('a') + ord(a) + n - ord('z') - 1)
                else:
                    answer += chr(ord(a) + n)
            # 대문자?
            else:
                if ord(a) + n > ord('Z'):
                    answer += chr(ord('A') + ord(a) + n - ord('Z') - 1)
                else:
                    answer += chr(ord(a) + n)
        else:
            answer += ' '
    return answer