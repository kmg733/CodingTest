# 종말의 숫자는 666, 1666, 2666, ... , 5666, 6660, 6666 이런순서다. 

n = int(input())
count = 0
title = 666

while True:
    if '666' in str(title):
        count += 1   
        if count == n:
            print(title)
            break
    title += 1