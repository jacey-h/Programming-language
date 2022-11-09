# def solution(s):
#     p_list = []
#     y_list = []
#     for i in list(str(s)):
#         if i == 'p' or i == 'P':
#             p_list.append(i)
#         elif i == 'y' or i == 'Y':
#             y_list.append(i)
#     if len(p_list) == len(y_list):
#         answer = True
#     else:
#         answer = False
#     return answer

def solution(s):
    if s.lower().count('p') == s.lower().count('y'):
        answer = True
    else:
        answer = False
    return answer