import sys

c = int(input())

for i in range(c):
    a = list(map(int, sys.stdin.readline().split()))
    sum = 0
    
    # avg = sum(a[1:]) / a[0]
    for j in a[1:]:
        sum += j
    avg = sum / a[0]

    cnt = 0
    for k in a[1:]:
        if k > avg:
            cnt += 1
    
    per = cnt/a[0]*100
    #print('%.3f'%per+'%')
    print('{:0.3f}%'.format(per))