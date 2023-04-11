# def solution(s):
#     if (len(s) == 4) or (len(s) == 6):
#         for i in list(s):
#             if ord(i) >= 65:
#                 return False
#             else:
#                 answer = True
#     else:
#         answer = False
#     return answer

def solution(s):
    if ((len(s) == 4) or (len(s) == 6)) and s.isdigit() == True:
        return True
    else:
        return False