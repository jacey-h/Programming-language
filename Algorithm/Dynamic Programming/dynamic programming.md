# 동적계획법

2가지 조건을 만족할 때, 사용가능

1. 최적 부분 구조  (퀵정렬도 여기 해당이지만 2번 만족못함)

큰문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있음

1. 중복되는 부분 문제

동일한 작은 문제를 반복적으로 해결해야됨

*점화식 생각하기*

예시) 피보나치 수열

![az.JPG](%E1%84%83%E1%85%A9%E1%86%BC%E1%84%8C%E1%85%A5%E1%86%A8%E1%84%80%E1%85%A8%E1%84%92%E1%85%AC%E1%86%A8%E1%84%87%E1%85%A5%E1%86%B8%20011bd0dced004d46adb5389bf46e5dd3/az.jpg)

```python
def fibo(x):
  if x==1 or x ==2:
    return 1
  return fibo(x-1)+fibo(x-2)
fibo(4) >>3
```

탑다운(메모이제이션) → 하향식

이전에 계산된 결과를 일시적으로 기록해 놓는 넓은 개념

```python
d =[0]*100
def fibo(x):
  
  if x==1 or x ==2:
    return 1
  if d[x]!=0:
    return d[x]      
  d[x] = fibo(x-1)+fibo(x-2)
  return d[x]
fibo(99) >> 218922995834555169026
```

보턴업 (동적계획법의 전형적인 형태) → 상향식

결과 저장용 리스트 DP테이블 사용

```python
d =[0]*100
def fibo(x):
  d[1] = 1
  d[2] = 1
  for i in range(3,x+1):
    d[i] = d[i-1]+d[i-2]
  return d[x]
fibo(99) >> 218922995834555169026
```

## 개미전사

![ghj.JPG](%E1%84%83%E1%85%A9%E1%86%BC%E1%84%8C%E1%85%A5%E1%86%A8%E1%84%80%E1%85%A8%E1%84%92%E1%85%AC%E1%86%A8%E1%84%87%E1%85%A5%E1%86%B8%20011bd0dced004d46adb5389bf46e5dd3/ghj.jpg)

연속된 식량창고에서 식량 가져올 수 없음

![x.JPG](%E1%84%83%E1%85%A9%E1%86%BC%E1%84%8C%E1%85%A5%E1%86%A8%E1%84%80%E1%85%A8%E1%84%92%E1%85%AC%E1%86%A8%E1%84%87%E1%85%A5%E1%86%B8%20011bd0dced004d46adb5389bf46e5dd3/x.jpg)

```python
n = int(input())
num = list(map(int,input().split()))

d=[0]*n
d[0] = num[0]
d[1] = max(num[0],num[1])  # 이미 1,2번째 중 큰거를 d배열에 넣음
for i in range(2,n):
  d[i]= max(d[i-1],(d[i-2]+num[i]))

print(d[n-1])
```

## 1로 만들기 👺너무어려움

![r.JPG](%E1%84%83%E1%85%A9%E1%86%BC%E1%84%8C%E1%85%A5%E1%86%A8%E1%84%80%E1%85%A8%E1%84%92%E1%85%AC%E1%86%A8%E1%84%87%E1%85%A5%E1%86%B8%20011bd0dced004d46adb5389bf46e5dd3/r.jpg)

![z.JPG](%E1%84%83%E1%85%A9%E1%86%BC%E1%84%8C%E1%85%A5%E1%86%A8%E1%84%80%E1%85%A8%E1%84%92%E1%85%AC%E1%86%A8%E1%84%87%E1%85%A5%E1%86%B8%20011bd0dced004d46adb5389bf46e5dd3/z.jpg)

ai= i를 1로 만들기 위한 최소 연산횟수  트리구조로 볼때 자기자신(루트)를 더해야 하니까 +1

![cv.JPG](%E1%84%83%E1%85%A9%E1%86%BC%E1%84%8C%E1%85%A5%E1%86%A8%E1%84%80%E1%85%A8%E1%84%92%E1%85%AC%E1%86%A8%E1%84%87%E1%85%A5%E1%86%B8%20011bd0dced004d46adb5389bf46e5dd3/cv.jpg)

```python
x = int(input())

d=[0]*100
for i in range(2,x+1):
  d[i] = d[i-1]+1
  if d[i]%2==0:
    d[i] = min(d[i],d[i//2]+1)
  elif d[i]%3==0:
    d[i] = min(d[i],d[i//3]+1)
  elif d[i]%5==0:
    d[i] = min(d[i],d[i//5]+1)
print(d[x])
```

## 효율적인 화폐구성

![aaaaa.JPG](%E1%84%83%E1%85%A9%E1%86%BC%E1%84%8C%E1%85%A5%E1%86%A8%E1%84%80%E1%85%A8%E1%84%92%E1%85%AC%E1%86%A8%E1%84%87%E1%85%A5%E1%86%B8%20011bd0dced004d46adb5389bf46e5dd3/aaaaa.jpg)

![hjj.JPG](%E1%84%83%E1%85%A9%E1%86%BC%E1%84%8C%E1%85%A5%E1%86%A8%E1%84%80%E1%85%A8%E1%84%92%E1%85%AC%E1%86%A8%E1%84%87%E1%85%A5%E1%86%B8%20011bd0dced004d46adb5389bf46e5dd3/hjj.jpg)

```python
n ,m = map(int,input().split())
array = []
for i in range(n):
  array.append(int(input()))

d = [10001]*(m+1)
d[0]=0
for i in range(n):
  for j in range(array[i], m+1):
    if d[j - array[i]] != 10001:
      d[j] = min(d[j], d[j-array[i]]+1)
if d[m]==10001:
  print(-1)
else:
  print(d[m])
```