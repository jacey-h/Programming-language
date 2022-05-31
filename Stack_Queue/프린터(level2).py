from collections import deque
def solution(priorities, location):
    queue = deque()
    for i in range(len(priorities)):
        queue.append([priorities[i],i])
    count =0
    while(1):
        if len(queue)==1:
            return count+1
        first = queue.popleft()
        tail = queue
        maxi= max(list(map(lambda x : x[0],tail)))
        if first[0]<maxi:
            queue.append(first)  
        else:
            count+=1
            if first[1]==location:
                return count