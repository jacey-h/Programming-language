def solution(numbers):
    answer= list(set(range(10)) - set(numbers))
    
    return sum(answer)