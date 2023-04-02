# def solution(s):
    
#     data = []
#     result = []
#     sum = 1
#     for i in range(1,len(s)//2+1): # 아이디어는 맞음
#         for j in range(len(s)-i):
#             if s[j] != s[j+i]:
#                 if sum == 1:
#                     data.append(s[j])
#                 data.append(str(sum)+s[j])
#                 sum = 1        
#             else:
#                 sum += 1
#         print(data)
#         result.append(len(''.join(data)))
            
#     return min(result)

# 정답
def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2+1):
        compressed =""
        prev = s[0:step]
        count = 1
        for j in range(step,len(s),step):
            if prev == s[j:j+step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer
