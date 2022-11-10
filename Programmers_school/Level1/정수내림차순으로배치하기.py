def solution(n):
    
    sort_n = (list(str(n)))
    sort_n.sort(reverse = True)
    
    answer = int(''.join(sort_n))
    return answer