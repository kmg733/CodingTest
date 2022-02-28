def solution(price, money, count):
    total = 0
    for m in range(1, count + 1):
        total += (m * price)
    if total - money > 0:
        answer = total - money
    else:
        answer = 0
    return answer