def solution(numbers):
    return sum(range(10)) - sum(numbers)

numbers = [1,2,3,4,6,7,8,0]
print(solution(numbers))