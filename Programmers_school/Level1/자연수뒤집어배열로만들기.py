def solution(n):
    list_n = list(str(n))
    
    answer = []
    for i in list_n[::-1]:
        answer.append(int(i))
    return answer

# def solution(n):
#     list_n = list(str(n))

#     return list(map(int,list_n[::-1]))