def solution(left, right):
    
    def divisor(num):
        if num == 1:
            return 1
        divisor = []
        for i in range(1,num):
            if num % i == 0:
                divisor.append(i)
                divisor.append(num//i)
        print(divisor)
        return len(set(divisor))
    
    answer = 0
    for i in range(left,right+1):
        if divisor(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer