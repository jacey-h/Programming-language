def solution(answers):
    a1 = [1,2,3,4,5]*2000
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]*1300
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1000
    count1 = 0
    count2 = 0
    count3 = 0
    answer = []
    for i in range(len(answers)):
        if a1[i] == answers[i]:
            count1 +=1
        if a2[i] == answers[i]:
            count2 +=1
        if a3[i] == answers[i]:
            count3 +=1
    maxi = max(count1,count2,count3)
    if maxi == count1:
        answer.append(1)
    if maxi == count2:
        answer.append(2)
    if maxi == count3:
        answer.append(3)
    return answer