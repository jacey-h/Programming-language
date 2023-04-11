# 정렬

- 선택정렬

정렬되지 않은 원소들 중에서 ‘최솟값’을 선택하여 정렬된 부분의 바로 오른쪽 원소와 교환

```python
array = []
for i in range(len(array)):
	min_index = i
	for j in range(i+1,len(array)):
		if array[min_index]>array[j]:
				min_index = j
	array[min_index],array[i] =array[i],array[min_index]
```

- 삽입정렬

정렬안된 부분의 왼쪽 원소를 정렬된 부분에 삽입

```python
array = []
for i in range(1,len(array)):
	for j in range(i,0,-1):
		if array[j]<array[j-1]:
			array[j],array[j-1] =array[j-1],array[j]
		else: break
```

- 퀵정렬

피벗보다 작으면 왼쪽, 크면 오른쪽으로 재귀적 정렬

```python
array=[]

def quick_sort(array, start, end):
	if start >= end:
		return
	pivot = start
	left = start +1
	right = end

	while(left<=right):
		while(left<=end and array[left]<=array[pivot]):
			left+=1
		while(right>start and array[right]>=array[pivot]):
			right-=1
		if(left>right):
			array[right],array[pivot] = array[pivot],array[right]
		else:
			array[right],array[left] = array[left],array[right]
	quick_sort(array,start,right-1)
	quick_sort(array,right+1,end)   
```

파이썬 특성 활용

```python
array = []

def quick_sort(array){
	if len(array)<=1:
		return array
	pivot = array[0]
	tail = array[1:]

	left_side = [x for x in tail x<=pivot]
	right_side = [x for x in tail x>pivot]
	return quick_sort(left_side) + [pivot] + quick_sort(right_side) 
```

 

- 계수정렬

카운트하면서 정렬

```python
array = []
count = [0]*(max(array)+1)

for i in range(len(array)):
	count[array[i]]+=1
for i in range(len(count)):
	for j in range(count[i]):
		print(i,end= ' ')
```

## 두 배열의 원소 교체

![ii.JPG](%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%85%E1%85%A7%E1%86%AF%200eb93c1785454467a856ac5f954e839f/ii.jpg)

```python
n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse= True)
for _ in range(k):
  swap = a.pop(0) # 이러면 안됨
  swap2 = b.pop(0)
  if swap<swap2:
    a.append(swap2)

print(sum(a))
```

```python
n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a.sort()
b.sort(reverse= True)
for i in range(k):
  if a[i]<b[i]:
    a[i],b[i]=b[i],a[i]
  else:
    break

print(sum(a))
```

여기서 pop을 했다가 if문에 해당안되면 그대로 pop한채로 한개가 적게 되므로 오류!!!!!!

## 프로그래머스 - K번째 수

```python
def solution(array, commands):
    result=[]
    for i in commands:
        tmp = array[(i[0]-1):(i[1])]
        tmp.sort()
        result.append(tmp[i[2]-1]) 
    return result
```

## 프로그래머스 - 가장큰수

이미 아이디어는 처음 풀때 다른사람 풀이를 보고 이해함

```python
num = [str(x)*3[:2] for x in numbers]
resu=[]
for i,j in numbers,num:
    resu.append(list(i,j))
result = sorted(resu,key= lambda x : x[1])
```

다 안짠 코드

두번째 풀때 num을 바꿔버리니까 힘듬

```python
def solution(numbers): 
    num = list(map(str, numbers)) 
    num.sort(key = lambda x : x*3, reverse = True) 
    return str(int(''.join(num)))
```

이렇게 lambda사용해서 바꾸는게 아니라 정렬할때만 사용하도록 해주면 바로 구할 수 있음

## 프로그래머스 - H-Index

내풀이

```python
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
                if count[i]==i: # 이부분을 빨리 못해서 총 47분 걸림
                    answer=count[i]
                    break

    return answer
```

다른사람의 풀이

```python
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
```

```python
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0
```