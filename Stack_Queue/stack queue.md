# 스택/큐

## 프로그래머스 - 기능개발

```python
def solution(progresses, speeds):
    temp=[]
    for i in range(len(progresses)):
        t = (100-progresses[i])//speeds[i]
        if (100-progresses[i])%speeds[i]!=0:
            t+=1
        temp.append(t)
------------------------
    result=[]
    while True:
        count = 0
        if len(temp)==0:
            break
        elif len(temp)==1:
            result.append(1)
            break
        first = temp.pop(0)
        count+=1
        for _ in temp:

            if temp[0]<=first:
                temp.pop(0)
                count += 1
            else: break
        result.append(count)
    return result
```

두번째 풀때 두문제 맞춰서 18점임

```python
import math
def solution(progresses, speeds):
    days = []
    answer = []
    
    for i in range(len(progresses)):
    #   days.append((100-(progresses[i]))//speeds[i]) 소숫점아래는 다 버리므로 11번 케이스 통과 못함 
        days.append(math.ceil((100-progresses[i]) / speeds[i])) 
------------------
    index=0

    for i in range(len(days)) :
        if days[index] < days[i] :      # 현재 인덱스의 작업일보다 큰 작업일이 나오면
            answer.append(i - index)    # 둘의 차이(배포 개수)를 추가 
            index = i                   # 현재 인덱스를 갱신
            
    answer.append(len(days) - index)  # for문을 빠져나오면 나보다 큰게 없는경우 총길이에서 나의 인덱스 뺴줌 
		return answer
```

```python
for i in range(len(progresses)):
        t = (100-progresses[i])//speeds[i]
        if (100-progresses[i])%speeds[i]!=0:
            t+=1
        temp.append(t)
```

```python
import math
for i in range(len(progresses)):
    #   days.append((100-(progresses[i]))//speeds[i]) 소숫점아래는 다 버리므로 11번 케이스 통과 못함 
        days.append(math.ceil((100-progresses[i]) / speeds[i])) 
```

ceil 쓰지 않아도 이부분은 구현가능

## 프로그래머스 - 주식가격

일단 문제 이해가 잘 안됬고 이해하고 풀때도 for문 if문 쓰는데에서 막힘

이게 정답 풀이

```python
def solution(prices):
    n = len(prices)
    result = [0]*n
    
    for i in range(n):
        for j in range(i+1,n):
            if prices[i]<=prices[j]:
                result[i]+=1   # ------> 이 방식으로 카운트다운 한거도 넣을 수 있음!!!!
            else:
                result[i]+=1
                break
    return result
```

내가 한 방법 엄청 헤맴!!!!!!!!!!!!!!!!

```python
def solution(prices):
    n = len(prices)
    result = [0]*n
    
    for i in range(n-1):
				cnt = 0
        for j in range(i+1,n):
            if prices[i]<=prices[j]:
                cnt+=1
								result.append(cnt)  #------> 이렇게 하니까 cnt 카운트다운한거를 result에 못넣어줌
            else:
                result.append(1)
    result.append(0)
    return result
```

이렇게 해야 내가 생간한 대로 할 수 있음!!!!!!!!!!!

```python
def solution(prices):
    n = len(prices)
    result = []
    
    for i in range(n-1):
        cnt = 0
        for j in range(i+1,n):
            cnt+=1
            if prices[i]>prices[j]:     
                break
        result.append(cnt)
    result.append(0)
    return result
```