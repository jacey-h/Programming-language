# 시뮬레이션과 완전 탐색

2차원 공간에서의 방향벡터가 자주 활용됨

![sa.JPG](%E1%84%89%E1%85%B5%E1%84%86%E1%85%B2%E1%86%AF%E1%84%85%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A7%E1%86%AB%E1%84%80%E1%85%AA%20%E1%84%8B%E1%85%AA%E1%86%AB%E1%84%8C%E1%85%A5%E1%86%AB%20%E1%84%90%E1%85%A1%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20aae676ec97154f6b954e64bc59406230/sa.jpg)

```python
# 동,북,서,남
dx = [0,-1,0,1]
dy = [1,0,-1,0]

# 현재 위치
x,y = 2,2
for i in range(4):
# 다음 위치
	nx = x + dx[i]
	ny = y + dy[i]
	print(nx,ny)
```

## 상하좌우

![KakaoTalk_20220517_231913000.jpg](%E1%84%89%E1%85%B5%E1%84%86%E1%85%B2%E1%86%AF%E1%84%85%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A7%E1%86%AB%E1%84%80%E1%85%AA%20%E1%84%8B%E1%85%AA%E1%86%AB%E1%84%8C%E1%85%A5%E1%86%AB%20%E1%84%90%E1%85%A1%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20aae676ec97154f6b954e64bc59406230/KakaoTalk_20220517_231913000.jpg)

```python
n = int(input())
s = list(input().split())

x=1
y=1

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for i in s:
  if i=='R':
    if y>=n : 
      y=n
    else: y +=1
  if i=='L':
    if y<=1 : y=1
    else : y -=1
  if i=='U':
    if x<=1 : x=1
    else : x -=1
  if i=='D':
    if x>=n : x=n
    else: x +=1
print(x,y,end=" ")
```

```python
n = int(input())
s = list(input().split())
x=1
y=1
dx = [0, 0, -1, 1] 
dy = [1, -1, 0, 0]
alp = ['R','L','U','D']

for i in s:
  for j in range(len(alp)):
    if i == alp[j]:
      nx = x + dx[j]  
      ny = y + dy[j]
  if nx<1 or nx>n or ny<1 or ny>n: #이걸 위해서 nx,ny 만들어줌
    continue
  x,y=nx,ny
print(x,y)
```

이렇게 좌표로 할때는 dx,dy 사용하기

내꺼는 하나의 테스트 케이스에는 맞아도 모든 경우에 적용안될 코드임

## 시각

![KakaoTalk_20220517_231913690.jpg](%E1%84%89%E1%85%B5%E1%84%86%E1%85%B2%E1%86%AF%E1%84%85%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A7%E1%86%AB%E1%84%80%E1%85%AA%20%E1%84%8B%E1%85%AA%E1%86%AB%E1%84%8C%E1%85%A5%E1%86%AB%20%E1%84%90%E1%85%A1%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20aae676ec97154f6b954e64bc59406230/KakaoTalk_20220517_231913690.jpg)

```python
h = int(input())
_h = list(range(h+1))
m = list(range(60))
s = list(range(60))
count = 0
for hour in _h:
  for min in m:
    for sec in s:
      if '3' in str(hour)+str(min)+str(sec):  # 이 부분
        count+=1
print(count)
```

 if hour==3 or min==3 or sec==3: → 3이면이 아니라 3이 포함되면임!

## 문자열 재정렬

![KakaoTalk_20220517_231914453.jpg](%E1%84%89%E1%85%B5%E1%84%86%E1%85%B2%E1%86%AF%E1%84%85%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%A7%E1%86%AB%E1%84%80%E1%85%AA%20%E1%84%8B%E1%85%AA%E1%86%AB%E1%84%8C%E1%85%A5%E1%86%AB%20%E1%84%90%E1%85%A1%E1%86%B7%E1%84%89%E1%85%A2%E1%86%A8%20aae676ec97154f6b954e64bc59406230/KakaoTalk_20220517_231914453.jpg)

모든 알파벳을 오름차순으로 정렬하여 출력한 뒤에, 그뒤에 모든 숫자를 더한 값을 이어서 출력합니다.

```python
s = input()
stri = []
for i in s:
  stri.append(i)
num = list(map(str,range(10)))

alp = [x for x in stri if x not in num]
number = [x for x in stri if x in num]
alp.sort()
summ = str(sum(map(int,number)))
alp.append(summ)
for i in alp:
  print(i,end="")
```

```python
s = input()
result =[]
value = 0

for i in s:
	if x.isalpha():
		result.append(x)
	else:
		value += int(x)
result.sort()
if value!=0:
	result.append(str(value))
print(''.join(result))
```

summ 이 0인지 아닌지 판단하는 구문 필요!

isalpha를 사용해서 쉽게 알파벳이랑 숫자를 구분할 수 있음

## 프로그래머스 - 모의고사

첫번쨰, 두번째 풀이가 완전 같음

```python
def solution(answers):

    n1 = [1, 2, 3, 4, 5] * 2000
    n2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1300
    n3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] *1000

    count1 ,count2,count3=0,0,0
    for i in range(len(answers)):
        if n1[i] == answers[i]:
            count1 +=1
        if n2[i] == answers[i]:
            count2 +=1
        if n3[i] == answers[i]:
            count3 +=1
    result = []
    maxi = max(count1,count2,count3)
    if maxi ==count1:
        result.append(1)
    if maxi ==count2:
        result.append(2)
    if maxi ==count3:
        result.append(3)
    result.sort()
    return result
```

다른 사람 풀이

```python
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):  # 이 부분이 내가 구현하고 싶었던 부분!!!!
        if s == max(score):
            result.append(idx+1)

    return result
```

## 프로그래머스 - 소수찾기 🧨🧨🧨🧨🧨🧨🧨🧨🧨다시

```python
from itertools import permutations
def solution(numbers):

    # 소수 찾는 함수
    def finds(x):
        for i in range(2,x):
            if x%i==0:
                return False
        return True

    # 문자열 끊어서 리스트로 받기
    num=[]
    for i in numbers:
        num.append(i)
    nlist=[]
    rlist=[]
    result=0

    # 순열을 이용해서 자릿수대로 뽑기 list(permutations(num,i+1)) 형태 기억하기
    for i in range(len(num)):
        nlist.append(list(permutations(num,i+1)))

    # int(''.join(j)) 형태 기억하기 -> 문자열 합쳐서 int형으로 바꿔줌
    for i in range(len(num)):
        for j in nlist[i]:
            rlist.append((int(''.join(j))))

    # 중복제거
    r = list(set(rlist))
    
    for i in range(len(r)):
        if r[i]==1 or r[i]==0:
            continue
        if finds(r[i]):
            result+=1
                         
    return result
```

순열뽑은걸 사용하는게 힘듬

한번에 print없이가 어려움

## 프로그래머스 - 카펫 → 20분컷 잘했음!

```python
def solution(brown, yellow):
    yx=[]
    yy=[]
    for i in range(1,yellow+1):
        if yellow%i==0:
            if i>=yellow//i:
                yx.append(i)
                yy.append(yellow//i)
    bx = [x+2 for x in yx]
    by = [x+2 for x in yy]
    
    for i in range(len(yx)):
        if yx[i]*yy[i] == yellow and (bx[i]*by[i]-yx[i]*yy[i])==brown:
            return [bx[i],by[i]]
```