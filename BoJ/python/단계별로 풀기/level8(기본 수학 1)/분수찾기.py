# 홀수일때 왼쪽이 큰수고 짝수일때 오른쪽이 큰수로 시작

X = int(input())

line = 1

while X > line:
    X -= line
    line += 1

if line % 2 == 0:
    left = X
    right = line - X + 1
else:
    left = line - X + 1
    right = X

print(str(left)+'/'+str(right))