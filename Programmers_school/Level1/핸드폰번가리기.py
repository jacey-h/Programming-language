def solution(phone_number):
    phone_list = list(phone_number[-4:])
    phone_len = len(phone_number)
    answer = '*'*(phone_len-4)+''.join(phone_list)
    return answer