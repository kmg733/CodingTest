def solution(sizes):
    w = 0
    h = 0
    for sizeA, sizeB in sizes:
        if sizeA >= sizeB:
            w = max(w, sizeA)
            h = max(h, sizeB)
        else:
            w = max(w, sizeB)
            h = max(h, sizeA)
    return w * h

# 다른 사람의 풀이
# def solution(sizes):
#     return max(max(x) for x in sizes) * max(min(x) for x in sizes)