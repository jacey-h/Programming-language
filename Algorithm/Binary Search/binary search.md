# 이진탐색

재귀함수

```python
def binary_search(array, target,start,end):
  if start>end:
    return None
  mid = (start+end)//2
  if target==array[mid]: 
    return mid
  elif target > array[mid]:  # 1,3,4,6,8  4
    return binary_search(array,target,mid+1,end)
  else:
    return binary_search(array,target,start,mid-1)
  
n = 10
target = 7
array = [1,3,5,7,9,11,13,15,17,19]

result = binary_search(array, target,0,n-1)
if result==None:
  print("원소가 존재하지 않습니다")
else: print(result+1)
```

반복문

```python
def binary_search(array, target,start,end):
  while start<=end:
    mid = (start+end)//2
    if array[mid]==target: return mid
    elif array[mid]>target:
      end = mid-1
    else:
      start=mid+1
  return None

n = 10
target = 7
array = [1,3,5,7,9,11,13,15,17,19]

result = binary_search(array, target,0,n-1)
if result==None:
  print("원소가 존재하지 않습니다")
else: print(result+1)
```

- 파이썬 이진탐색 라이브러리

`from bisect import bisect_left, bisect_right`

`bisect_left(a,x)`  : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환

`bisect_right(a,x)` : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환

값이 특정 범위에 속하는 데이터 개수 구하기

```python
from bisect import bisect_left, bisect_right

def count_num(array, left_value, right_value):
	left_index = bisect_left(array,left_value)
	right_index = bisect_right(array, right_value)
	return right_index - left_index

array = [1,2,3,3,3,3,4,4,8,9]
# 값이 4인 데이터의 개수
print(count_num(array,4,4))  >>2
# 범위[-1,3] 안에 있는 데이터 개수
print(count_num(array,-1,3))  >>6
```

## 떡볶이 떡 만들기

![llk.JPG](%E1%84%8B%E1%85%B5%E1%84%8C%E1%85%B5%E1%86%AB%E1%84%90%E1%85%A1%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20a56ff79dcc3244a59f3f2a4c8326b199/llk.jpg)

```python
n,m = map(int,input().split())
h = list(map(int,input().split()))
start = 1
end = max(h)
result = 0
while start<=end:
  mid = (start+end)//2
  cut = 0
  for i in h:
    if i>mid:     # 떡의 길이가 더 길때 잘라줘야함
      cut += (i-mid)
  if cut==m:
    result = mid
    break
  elif cut>m:
    result = mid
    start = mid+1
  else:
    end = mid-1
print(result)
```

## 프로그래머스 - 입국심사

```python
def solution(n, times):
    start = min(times)
    end = max(times)*n
    result=[]
    while start<=end:
        mid = (start+end)//2
        tmp = 0
        for i in times:
            tmp += (mid//i)
            if tmp>=n:  -> 이렇게하고 나가야 불필요한 계산줄일수 있음
                break
        if tmp == n:       -> break문도 없어서 계속 실행하게 함!! 오류발생
            result.append(mid)
        elif tmp>=n:
            result.append(mid)
            end = mid-1
        else:
            start = mid +1
    return min(result)
```

```python
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
```

위의 2가지 점 뺴면 똑같이 짰음 물론 이진탐색으로 푸는 아이디어 고민하는게 젤 어려움!