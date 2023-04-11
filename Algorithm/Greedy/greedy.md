# 그리디

## 1이 될때까지 →동적계획법이랑 다름!!!

![KakaoTalk_20220517_231910775.jpg](%E1%84%80%E1%85%B3%E1%84%85%E1%85%B5%E1%84%83%E1%85%B5%205003a753237641c7b5dd6c9006803885/KakaoTalk_20220517_231910775.jpg)

1번 : N에서 1을 빼기

2번 :  N을 K로 나누기

```python
n,k = map(int,input().split())
count = 0
while n!=1:
  
  if n%k!=0:
    n-=1
    count+=1
  else:
    n= n//k
    count +=1
print(count)
```

```python
n,k = map(int,input().split())
result = 0
while True:
  target = (n//k)*k
  result += (n-target)
  n = target

  if n<k:
    break
  result += 1
  n//=k

result += (n-1)
print(result)
```

내가 짠 코드 / 강의 정답

## 곱하기 혹은 더하기

![KakaoTalk_20220517_231911559.jpg](%E1%84%80%E1%85%B3%E1%84%85%E1%85%B5%E1%84%83%E1%85%B5%205003a753237641c7b5dd6c9006803885/KakaoTalk_20220517_231911559.jpg)

왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 x 혹은 + 연산자를 넣어 가장 큰 수 만들기

모든 연산은 왼쪽부터 순서대로

```python
s = input()
num = []
for i in s:
  num.append(int(i))

result = num[0]
for i in range(len(num)-1):
  if num[i] ==0 or num[i] ==1:  # 정답에선 num[i]<=1 or result <=1
    result += num[i+1]
  else:
    result *= num[i+1]
print(result)
```

## 모험가 길드

![KakaoTalk_20220517_231912356.jpg](%E1%84%80%E1%85%B3%E1%84%85%E1%85%B5%E1%84%83%E1%85%B5%205003a753237641c7b5dd6c9006803885/KakaoTalk_20220517_231912356.jpg)

공포도가 x인 모험가는 반드시 x명 이상으로 구성된 그룹에 참가

```python
n = int(input())
x = list(map(int,input().split()))
x.sort()
count = 0
temp = []
for i in range(n):
  temp.append(x[i])
  if x[i] <= len(temp):
    count += 1
    temp=[]
print(count)
```

## 프로그래머스 - 체육복

2번째 풀은거 (스스로)

```python
def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    count = 0
    _lost = [x for x in lost if x not in reserve]
    _reserve = [x for x in reserve if x not in lost]
    if len(lost)!= len(_lost): count += (len(lost)-len(_lost))

    for i in _lost:
        for j in _reserve:
            if j == (i-1) or j == (i+1):
                count+=1
                _reserve.pop(0)
                break
            if _reserve==[]: break
    result = n-(len(lost))+count
    return result
```

첫번째 도움받아서

```python
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    _lost.sort()
    _reserve.sort()
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
```

for문 중첩문 사용하는 것보다 for문 안에 if문 사용이 더 좋은거 같음!