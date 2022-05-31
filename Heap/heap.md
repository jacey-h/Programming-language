# 힙

- 힙 생성

```python
import heapq
heap =[]
```

- 힙 추가

```python
heapq.heappush(heap,1)
```

- 힙 삭제

```python
heapq.heappop(heap)
```

- 기존 리스트를 힙으로 반환

```python
nlist = [2,5,7]
heapq.heapify(nlist)
```

- 최대힙

```python
import heapq
nums = [2,4,5,7,9]
heap=[]
for num in nums:
	heapq.heappush(heap,(-num,num)) #(우선순위,값)
for _ in range(len(heap)):
	print(heapq.heappop(heap)[1]) # 값을 읽어옴
```

- k번째 최소값/ 최댓값

```python
import heapq

def kth(nums,k):
	heap=[]
	for num in nums:
		heapq.heappush(heap,num)
	kth_min=0
	for _ in range(k):
		kth_min = heapq.heappop(heap)
	return kth_min
```

- 힙정렬

```python
import heapq

def heap_sort(nums):
  heap = []
  for num in nums:
    heapq.heappush(heap, num)

  sorted_nums = []
  while heap:
    sorted_nums.append(heapq.heappop(heap))
  return sorted_nums

print(heap_sort([4, 1, 7, 3, 8, 5]))
```

[[파이썬] heapq 모듈 사용법](https://www.daleseo.com/python-heapq/)

## 프로그래머스 - 더맵게

두번째

```python
def solution(scoville, K):        
    import heapq
    heapq.heapify(scoville)
    count=0
    while scoville:
        if len(scoville)==1:
            f= heapq.heappop(scoville)
            if f<K: 
                return -1
                break
            else: break
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        if first<K or second<K:
            tmp = first+(second*2)
            heapq.heappush(scoville,tmp)
            count+=1
        else: break
    return count
```

첫번째

```python
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
```

처음 푼게 더 정돈된 느낌이 듬 그치만 둘다 정답!