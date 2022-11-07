def solution(absolutes, signs):
    answer = 0
    for i,j in zip(signs,absolutes):
        if i==True:
            answer = answer + j
        else:
            answer = answer -j
    return answer