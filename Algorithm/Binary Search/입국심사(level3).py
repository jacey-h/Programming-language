def solution(n, times):
    answer=0
    start =min(times)
    end = max(times)*n
    while start<=end:
        mid = (start+end)//2
        temp=0
        for i in times:
            temp += (mid//i)
            if temp>=n:   #mid분 동안 n명이상의 심사가능하면 빠져나감
                break
        if temp>=n:
            answer =mid
            end = mid-1
        elif temp<n:
            start = mid+1
    return answer