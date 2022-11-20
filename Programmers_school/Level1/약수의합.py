# def solution(n):
#     answer = []
#     for i in range(n+1):
#         for j in range(i,n+1):
#             if i*j == n:
#                 answer.append(i)
#                 answer.append(j)
#     return sum(set(answer))

def solution(n):
    answer = [n]
    for i in range(1,n//2+1):
        if n % i == 0:
            answer.append(i)
    return sum(answer)