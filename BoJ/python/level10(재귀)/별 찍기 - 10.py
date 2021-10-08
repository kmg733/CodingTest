import sys
sys.setrecursionlimit(10**6)

def makeStar(len):
    if len == 1:
        return ['*']

    stars = makeStar(len // 3)
    starList = []

    for i in stars:
        starList.append(i * 3)
    for i in stars:
        starList.append(i + ' ' * (len // 3) + i)
    for i in stars:
        starList.append(i * 3)
    return starList

n = int(sys.stdin.readline())
print('\n'.join(makeStar(n)))

# 참고: https://cotak.tistory.com/38