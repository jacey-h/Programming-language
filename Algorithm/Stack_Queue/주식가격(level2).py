def solution(prices):
    n = len(prices)
    result = [0]*n

    for i in range(n):
        for j in range(i+1,n):
            if prices[i]<=prices[j]:
                result[i]+=1
            else:
                result[i]+=1
                break
    return result