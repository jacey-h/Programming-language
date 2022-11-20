def solution(price, money, count):
    re_money = []
    for i in range(1, count+1):
        re_money.append(price*i)
    result = money - sum(re_money)
    
    if result < 0:
        answer = sum(re_money) - money
    else: 
        answer = 0

    return answer