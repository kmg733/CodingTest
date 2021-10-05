# [::-1]을 이용한 역순출력
a, b = input().split()
a = int(a[::-1])
b = int(b[::-1])

if(a > b):
    print(a)
else:
    print(b)

# 다른 방법 - reversed와 join을 이용한 역순출력
# a, b = input().split()
# a = int(''.join(reversed(a)))
# b = int(''.join(reversed(b)))

# if(a > b):
#     print(a)
# else:
#     print(b)
