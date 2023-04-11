# 해시

## 프로그래머스 - 완주하지 못한 선수

```python
def solution(participant, completion):
    from collections import Counter

    result = Counter(participant) - Counter(completion)
    return(str(list(result)[0]))
```

```python
def solution(participant, completion):
    participant.sort()
    completion.sort()
    num = len(completion)

    for idx in range(num) :
        if participant[idx] != completion[idx] : return participant[idx]
    return participant[num]
```

## 프로그래머스 - 전화번호 목록

```python
def solution(phone_book):
    index = 0
    while True:  # while문 돌려서 효율성 2문제 못맞힘
 
        for i in range(len(phone_book)):
            if index!=i and len(phone_book[index])<=len(phone_book[i]):
                if phone_book[index] == phone_book[i][:len(phone_book[index])]:
                    return False
        index +=1
        if index==len(phone_book):
            return True
```

```python
def solution(phone_book):
    phone_book.sort() # -> 무조건 i랑 i+1을 비교하니까 sort해줘야함
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])] :
            return False
    return True
```

## 프로그래머스 - 위장

![kkkk.JPG](%E1%84%92%E1%85%A2%E1%84%89%E1%85%B5%20df6ec58df84240cd97f21672b39fa893/kkkk.jpg)

이 아이디어를 못 떠올려서 스스로 못풀음 대신 이 아이디어로 코드짠거

```python
from collections import Counter
def solution(clothes):
    cnt=[]
    for i in range(len(clothes)):
        cnt.append(clothes[i][1])
    count = Counter(cnt)
    clist = list(count.values())

    if len(clist)==1: 
        return clist.pop()
    else:
        csum = [x+1 for x in clist]
        mul=1
        for i in csum:
            mul*=i
    return mul-1
```

다른사람의 해쉬맵 사용한 풀이 

```python
def solution(clothes):
    # 1. 옷을 종류별로 구분하기
    hash_map = {}
    for clothe, type in clothes:
        hash_map[type] = hash_map.get(type, 0) + 1
        
    # 2. 입지 않는 경우를 추가하여 모든 조합 계산하기
    answer = 1
    for type in hash_map:   
        answer *= (hash_map[type] + 1)
    
    # 3. 아무종류의 옷도 입지 않는 경우 제외하기
    return answer - 1

```

딕셔너리 다시보기