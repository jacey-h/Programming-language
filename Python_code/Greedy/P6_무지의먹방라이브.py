# # 효율성 0점 풀이
# def solution(food_times, k):
#     food_list = []
#     while sum(food_times):
#         for j in range(len(food_times)):
#             if food_times[j] != 0:
#                 food_list.append(j+1)
#                 food_times[j] -= 1
                
#     answer = food_list[k]
#     return answer
# 수정 후 정확성 100/ 효율성 0
# def solution(food_times, k):
#     food_list = []
#     cnt = 0
#     if sum(food_times) <= k:
#          return -1
#     while 1:
#         for j in range(len(food_times)):
#             if food_times[j] == 0:
#                 continue
#             else:
#                 food_times[j] -= 1
#                 food_list.append(j+1)
#             cnt += 1
#             if cnt == k+1:
#                 return food_list[k]

import heapq
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i], i+1))
        
    sum_value = 0
    previous = 0
    length = len(food_times)
    
    while sum_value + ((q[0][0]-previous)*length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous)*length
        length -= 1
        previous = now
        
    result = sorted(q, key = lambda x: x[1])
    return result[(k-sum_value)%length][1]
    

