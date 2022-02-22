# https://programmers.co.kr/learn/courses/30/lessons/81301
def solution(s):
    word = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    for w, d in word.items():        
        s = s.replace(w, d)
    return int(s)

s = "one4seveneight"
print(solution(s))