def solution(s):
    slen = len(s)
    if slen % 2 == 1:
        answer = str(s[slen//2])
    else:
        answer = str(s[slen//2-1:slen//2+1])
    return answer 