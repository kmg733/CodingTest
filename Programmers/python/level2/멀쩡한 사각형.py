import math
# 규칙을 찾는문제임.
# 참고: https://leedakyeong.tistory.com/135#comment16270807
def solution(w,h):    
    return w * h - (w + h - math.gcd(w, h))