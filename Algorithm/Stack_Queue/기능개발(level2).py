import math
def solution(progresses, speeds):
    days = []
    answer = []

    for i in range(len(progresses)):
    #   days.append((100-(progresses[i]))//speeds[i]) 소숫점아래는 다 버리므로 11번 케이스 통과 못함 
        days.append(math.ceil((100-progresses[i]) / speeds[i])) 
    index=0

    for i in range(len(days)) :
        if days[index] < days[i] :      # 현재 인덱스의 작업일보다 큰 작업일이 나오면
            answer.append(i - index)    # 둘의 차이(배포 개수)를 추가 
            index = i                   # 현재 인덱스를 갱신

    answer.append(len(days) - index)
    return answer