def solution(n):
    mod = []
    while n >=3:
        mod.append(str(n%3))
        n = n//3
    mod.append(str(n))
    answer = int(''.join(mod),3)

    return answer