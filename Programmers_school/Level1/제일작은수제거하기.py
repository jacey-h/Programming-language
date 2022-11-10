# def solution(arr):
#     small_arr = min(arr)
#     answer = []
#     if len(arr) == 1:
#         answer.append(-1)
#     else:
#         for i in arr:
#             if i != small_arr:
#                 answer.append(i)
    
#     return answer

def solution(arr):
    small_arr = min(arr)

    if len(arr) == 1:
        answer = [-1]
    else:
        arr.remove(small_arr)
        answer = arr
    
    return answer