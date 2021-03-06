# Python TIL

- 산술연산자

| / | 나눗셈 (몫) |
| --- | --- |
| % | 나눗셈 (나머지) |
| ** | 거듭제곱 |
- 기타연산자

x in 리스트 → 있으면 참

x not in 문자열 → 없으면 참

- 변수설정
1. 첫번쨰문자에 숫자사용x
2. 예약어 사용하지 않음

- 문자열 다루기

`text = ‘hello’`

1. 대문자 변환 `text.upper()`
2. 소문자 변환 `text.lower()`
3. 지정한 문자 몇개있는지 세기 `text.count(’l’)`  >> 2

- 리스트형

`list = [리스트1, 리스트2, 리스트3]` → [대괄호]사용! 쉼표, 사용!

1. 값부르기 text[0]  >> 리스트1
2. 추가 `list.append(’리스트4’)`
3. 삭제 `list.remove(’리스트1’)` → 여러개이면 하나만 제거
4. 삽입 `list.insert(a,b)` : a번째 위치에 b 삽입
5. 끄집어내기 `list.pop()`  → 마지막꺼 끄집어냄
6. 순서바꾸기 `list.sort()`→ 문자열형은 알파벳순서, 숫자형은 낮은수부터 (오름차순)
7. `list.sort(reverse = True)` → 내림차순
8. 뒤집기 `list.reverse()`
9. 몇번째인지 찾기 `list.index(리스트안의 항목)`
10. `list.count(리스트1)` → 특정값을 가지는 데이터의 개수 세기
11. 리스트 컴프리헨션 `array = [i for i in range(10)]` >> [0,1,2,3,4,5,6,7,8,9]

```python
# 0~19까지의 수 중 홀수만
array = [i for i in range(20) if i%2==1]  

# 1~9까지의 수들의 제곱값
array = [i*i for i in range(1,10)]
```

1. 각 자릿수를 나눠 리스트로 만들기

```python
s = 1234567 
n = list(map(int,str(s))) 
print(n) # [1,2,3,4,5,6,7]
```

예시) 리스트에서 특정값을 가지는 원소 모두 제거하기

```python
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
result = [i for i in a if i not in remove_set]  >> [1, 2, 4]
```

- 딕셔너리형

`dic = {key1 : value1 , key2 : value2}` → 키와 데이터는 :으로! 쉼표사용! 중괄호 사용!

1. 키값으로 데이터 부르기 `dic[key1]` → 대괄호 사용!
2. 키값 다 부르기 `dic.keys()`
3. 데이터값 다 부르기 `dic.values()`
4. for문

for문을 통해 딕셔너리를 for문을 돌리면 key값이 할당

```python
>>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> for key in a:
...     print(key)
... 
alice
bob
tony
suzy
```

value값으로 for문을 반복하기 위해서는 `values()`를 사용

```python
>>> for val in a.values():
...     print(val)
... 
[1, 2, 3]
20
15
30
```

key와 value를 한꺼번에 for문을 반복하려면 `items()`를 사용

```python
>>> for key, val in a.items():
...     print("key = {key}, value={value}".format(key=key,value=val))
... 
key = alice, value=[1, 2, 3]
key = bob, value=20
key = tony, value=15
key = suzy, value=30
```

- 튜플형 ❗**만든 후 바꿀수없음**

`tuple = (요소1, 요소2, 요소3)` → 소괄호 사용! 쉼표사용!

- 집합(set)형

`set = {요소1, 요소2, 요소3}` → 중괄호 사용! 쉼표사용!

1. 집합형 만들기 `taste = set(’delicious’)` >> `{’d’, ‘u’, ‘s’, ‘l’, ‘e’, ‘o’, ‘c’, ‘i’}` → i가 두개이지만 하나밖에 안씀! 알파벳순으로!
2. set함수 사용해도 문자 단위로 분리되지 않으려면 리스트 시용하기
    
    fruit = [’apple’, ‘banana’, ‘mango’]
    
    taste = set(fruit) >> {’apple’, ‘banana’, ‘mango’}
    
3. 추가 `taste.add(4)` : 한개 추가/ `taste.update([’kiwi’])` : 여러개 추가 → 대괄호 사용해서 리스트로 넘겨야 분리되지 않음❗
4. 삭제 `taste.remove(’d’)`
5. 중복 제거 기능
6.  복수 데이터 간 계산
    
    
    | 기호 | 기능 |
    | --- | --- |
    | A <= B | B에 A의 모든 요소가 포함되는지 조사 |
    | A >= B | A에 B의 모든 요소가 포함되는지 조사 |
    | A | B | 합집합 생성 |
    | A & B | 교집합 생성 |
    | A - B | A에는 포함되는데 B에는 포함되지 않는 집합 생성 |
    | A ^ B | 한쪽 밖에 포함하지 않은 집합 생성 |
- if문

```python
if (조건식):
	실행할 문장 1  # 만약 아무것도 처리하고 싶지 않을때 pass 를 사용한다
	pass

elif (조건식):
	실행할 문장 2

else:
	실행할 문장 3

```

- 조건 묶기
1. or 연산자
2. and 연산자

for문

[for문 사용법](Python%20TIL%20e600a2e6f37040809812443e2d7fa4aa/for%E1%84%86%E1%85%AE%E1%86%AB%20%E1%84%89%E1%85%A1%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%87%E1%85%A5%E1%86%B8%2017feed53e8944082a866a954d4819c69.md)

```cpp
for 변수 in range(반복하고 싶은 횟수):
	반복 실행할 문장
```

**`range(start, stop, step)`**

```cpp
for 변수 in 리스트형:
	반복 실행할 문장(변수에는 리스트의 각 요소가 대입됨)
```

```cpp
for 변수 in 딕셔너리형:
	반복 실행할 문장(변수에는 키(key)가 대입됨)
```

언더바  사용하기

```python
for _ in range(5):
	print("hello world") # 반복을 위한 변수의 값을 무시하고자 할 때
```

**for문 사용법**

- for문 루프가 종료된 후 어떤 작업을 수행할때 → else사용

```python
l = ['Alice', 'Bob', 'Charlie']
 
for name in l:
    print(name)
else:
    print('!!FINISH!!')
# Alice
# Bob
# Charlie
# !!FINISH!!
```

- enumerate함수

```python
l = ['Alice', 'Bob', 'Charlie']
 
for name in l:
    print(name)
# Alice
# Bob
# Charlie
 
for i, name in enumerate(l):
    print(i, name)
# 0 Alice
# 1 Bob
# 2 Charlie
```

```python
for i, name in enumerate(l, 1):
    print(i, name)
# 1 Alice
# 2 Bob
# 3 Charlie
 
for i, name in enumerate(l, 42):
    print(i, name)
# 42 Alice
# 43 Bob
# 44 Charlie
```

- zip함수

```python
names = ['Alice', 'Bob', 'Charlie']
ages = [24, 50, 18]
 
for name, age in zip(names, ages):
    print(name, age)
# Alice 24
# Bob 50
# Charlie 18
```

LIST의 여러 개체(목록)에서 요소와 인덱스(카운터)를 동시에 얻으려면 enumerate(), zip() 함수를 함께 사용

```python
names = ['Alice', 'Bob', 'Charlie']
ages = [24, 50, 18]
 
for i, (name, age) in enumerate(zip(names, ages)):
    print(i, name, age)
# 0 Alice 24
# 1 Bob 50
# 2 Charlie 18
```

- reversed함수

```python
l = ['Alice', 'Bob', 'Charlie']
 
for name in reversed(l):
    print(name)
# Charlie
# Bob
# Alice
```

```python
for i, name in reversed(list(enumerate(l))):
    print(i, name)
# 2 Charlie
# 1 Bob
# 0 Alice
```

```python
for i, name in enumerate(reversed(l)):
    print(i, name)
# 0 Charlie
# 1 Bob
# 2 Alice
```

### 다중루프

```python
l1 = [1, 2, 3]
l2 = [10, 20, 30]
 
for i in l1:
    for j in l2:
        print(i, j)
# 1 10
# 1 20
# 1 30
# 2 10
# 2 20
# 2 30
# 3 10
# 3 20
# 3 30
```

중첩 for문 없이 다중루프 돌리는법

```python
from itertools import product
 
l1 = [1, 2, 3]
l2 = [10, 20, 30]
 
for i, j in product(l1, l2):
    print(i, j)
# 1 10
# 1 20
# 1 30
# 2 10
# 2 20
# 2 30
# 3 10
# 3 20
# 3 30
```

- while문

```cpp
while(조건식):
	반복 실행할 문장
```

`break`문 → 무조건 반복문(for,while) 블록 밖으로 탈출

`continue`문 → 무조건 블록끝으로 건너뛴 후 다시 반복문 처음으로 돌아감

- 함수

```python
def 함수의 이름():
	처리 1
	처리 2
	return result
```

[내장함수](Python%20TIL%20e600a2e6f37040809812443e2d7fa4aa/%E1%84%82%E1%85%A2%E1%84%8C%E1%85%A1%E1%86%BC%E1%84%92%E1%85%A1%E1%86%B7%E1%84%89%E1%85%AE%20f032388f320e482c8bdd700ee1ae5025.md)

- 예외 처리

```python
try:
	처리 A(에러가 발생하는 처리)
except Exception as e:
	처리 B
print(e.args)(예외의 내용을 출력)
```

- 클래스

설계도 → 제품 : 클래스 → 인스턴스

```python
class 클래스 이름:
	변수 정의 (멤버 변수)
	함수 정의 (메소드) # 정의 할때 def 함수이름(self) -> self 꼭 사용!clas
```

```python
class fruit:
	color = 'red'
	def taste(self):
		return 'delicious'

>> apple = fruit()
>> apple.color
'red'
>> apple.taste()
'delicious'
```

```python
class Circle:
	radius = 10
	def getArea(self):
		return 3.14*self.radius*self.radius
```

```python
class 클래스 이름:
	def__init__(self, 인자, ...)
		self.초기 설정하고 싶은 변수 = 인자
		초기 수행 처리
	def 메소드(함수) 이름:
		메소드 처리
```

```python
class Circle:
	def__init__(self,r): # 이렇게 하면 radius를 10이 아닌 원하는 걸로 사용가능
		self.radius = r
	def getArea(self):
		return 3.14*self.radius*self.radius

>> onecircle = Circle(1)
>> onecircle.getArea
3.14i
```

자료구조 알고리즘에서 배웠음

```python
class SList:
  class Node:
    def __init__(self, item, link):
      self.item = item
      self.next = link
  
  def __init__(self):
    self.head = None
    self.size = 0

  def size(self): return self.size
  def is_empty(self) : return self.size == 0

  def insert_front(self, item):
    if self.is_empty():
      self.head = self.Node(item, None)
    else:
      self.head = self.Node(item, self.head)
    self.size += 1
```

## 표준라이브러리

- **itertools → 순열과 조합**

순열 : 서로 다른 n개에서 서로 다른 r개를 선텍하여 일렬로 나열

```python
from itertools import permutations

data = [’A’, ‘B’, ‘C’]

result = list(permutations(data,3))
```

중복순열 `product`

중복조합 `combinations_with_replacement`

조합 : 서로 다른 n개에서 순서에 상관없이 서로 다른  r개를 선택하는 것 → ‘abc’랑 ‘acb’랑 같음

```python
from itertools import combinations

data = [’A’, ‘B’, ‘C’]

result = list(combinations(data,2))
```

- heapq → 힙 자료구조 (우선순의 큐 )
- bisect → 이진탐색
- collections → 덱, 카운터

카운터 : 등장 횟수를 세는 기능 제공 → 내부의 원소가 몇번씩 등장했는지 알려줌

```python
from collections import Counter

count = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(count['blue']) >> 3
print(dict(count)) >> {'red':2, 'blue':3, 'green': 1}
```

카운터 기능

1. 빼기, 더하기

```python
from collections import Counter
count1 = Counter('aabbccdd')
count2 = Counter('aabbccd')

print(count1) >> Counter({'a': 2, 'b': 2, 'c': 2, 'd': 2})
print(count2) >> Counter({'a': 2, 'b': 2, 'c': 2, 'd': 1})

cnt = count1-count2
print(cnt)  >> Counter({'d': 1})
```

1. 상위요소 반환 `**.most_common(출력개수)` → 상위 몇개의 요소 출력**
2. 각 요소의 값 각각 빼주기 `**count1.subtract(count2)` → count1에서 2를 요소별로 각각 뺴줌**
3. 교집합 `**count1&count2**` , 합집합 `**count1|count2**`
4. 카운터 숫자만큼 요소 반환 `**.elements()**`

```python
>>> cnt = Counter(a=5,b=3)
>>> cnt
Counter({'a': 5, 'b': 3})
>>> list(cnt.elements())
['a', 'a', 'a', 'a', 'a', 'b', 'b', 'b']
>>> list(cnt)
['a', 'b'] #-> 바로 리스트로 바꾸면 개수에 맞춰서 바꿀수 없음
```

- math → 팩토리얼, 제곱근, 최대공약수,파이 등

```python
import math

# 최소 공배수를 구하는 함수
def lcm(a,b):
	return a*b // math.gcd(a,b) 
a=21
b=14

print(math.gcd(21,14))  # 최대 공약수 >>7
print(lcm(21,14)) # 최소 공배수 >> 42
```

- operator

```python
>>> from operator import itemgetter, attrgetter

>>> sorted(student_tuples, key=itemgetter(2))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

>>> sorted(student_objects, key=attrgetter('age'))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

키함수 사용할 경우

```python
>>> student_tuples = [
...     ('john', 'A', 15),
...     ('jane', 'B', 12),
...     ('dave', 'B', 10),
... ]
>>> sorted(student_tuples, key=lambda student: student[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

[Sorting HOW TO - Python 3.10.4 documentation](https://docs.python.org/ko/3/howto/sorting.html)