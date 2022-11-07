def solution(n):
    answer = []
    for i in range(2,n):
        if n % i == 1:
            answer.append(i)
    answer.sort
    return answer[0]