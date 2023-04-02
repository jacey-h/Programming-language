def solution(N, stages):
    answer = []
    stages.sort()
    for i in range(1,N+1):
        m = 0
        s = 0
        for j in stages:
            if i == j:
                s += 1
            if i <= j:
                m += 1
        if s == 0:
            answer.append((i,0))
        else:
            answer.append((i,s/m))
        
    answer.sort(key = lambda x: x[1], reverse = True)
    result = list([i[0] for i in answer])
    return result