s = input().lower()
wordList = sorted(set(s))
cnt = []

for i in wordList:
    count = s.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    # find는 문자열에서만 사용가능하다. 
    # 때문에 리스트의 인덱스를 찾을때는
    # find대신 index를 사용한다.
    print(wordList[cnt.find(max(cnt))].upper())