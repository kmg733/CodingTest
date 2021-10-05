import sys

s = sys.stdin.readline().strip()
result = []

for i in range(ord('a'), ord('z')+1):
    if s.find(chr(i)) == -1:
        result.append(-1)
    else:
        result.append(s.find(chr(i)))
        
for i in result:
    print(i, end=" ")

# 숏코딩
# word = input()
# alphabet = list(range(ord('a'), ord('z')+1))  # 아스키코드 숫자 범위

# for x in alphabet :
#     print(word.find(chr(x)), end=" ") 