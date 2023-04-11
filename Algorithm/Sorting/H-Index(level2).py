def solution(citations):

    citations.sort()
    answer = 0
    n = len(citations)
    count = [0]*(n+1)
    for i in range(n+1):
        count[i] = 0
        for j in citations:
            if j>=i:
                count[i]+=1 
                if count[i]==i:
                    answer=count[i]
                    break

    return answer