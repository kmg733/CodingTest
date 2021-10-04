import sys

T = input()
T = int(T)
for i in range(1, T+1):
    a, b = sys.stdin.readline().split()
    a = int(a)
    b = int(b)
    #출력참고:https://docs.python.org/ko/3/tutorial/inputoutput.html
    #print('Case #'+str(i)+':', a+b)
    #print('Case #%d: %d'%(i, a+b))
    print('Case #{}: {}'.format(i, a+b))