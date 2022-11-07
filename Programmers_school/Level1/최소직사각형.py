def solution(sizes):
    w = 0
    h = 0
    for first, second in sizes:
        if first < second:
            first, second = second, first
        w = max(w, first)
        h = max(h, second)
    return w*h