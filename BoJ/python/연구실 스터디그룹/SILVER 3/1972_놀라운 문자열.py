# https://solved.ac/search?query=1972
import sys
input = sys.stdin.readline

def surprisingWord(word):
    isSp = True

    # i는 d-쌍(거리)을 의미함
    for i in range(1, len(word)):
        dWord = []

        # j는 부분 문자열을 의미함 
        for j in range(len(word) - i):
            # "ZGBG" 라는 문자열이 주어지면 순서대로
            # i = 1 "ZG", "GB", "BG"
            # i = 2 "ZB", "GG"
            # i = 3 "ZG"
            dWord.append(word[j] + word[j + i])
        for j in range(len(dWord) - 1):
            if dWord[j] in dWord[j + 1:]:
                isSp = False
    return isSp

while True:
    word = input().strip()
    if word == "*":
        break
    
    if surprisingWord(word):
        print(f"{word} is surprising.")
    else:
        print(f"{word} is NOT surprising.")


# 구현
# 자료 구조
# 문자열
# 해시를 사용한 집합과 맵