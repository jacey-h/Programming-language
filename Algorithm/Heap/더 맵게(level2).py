import heapq
def solution(scoville, K):
    heap = []
    for num in scoville:
        heapq.heappush(heap,num)
    count = 0
    while(1):
        first = heapq.heappop(heap)
        if first>=K: return count
        second = heapq.heappop(heap)
        heapq.heappush(heap,(first+second*2))
        count+=1
        if len(heap)==1:
            tmp = heapq.heappop(heap)
            if tmp>K: return count
            else: return -1