# 내장함수

[점프 투 파이썬](https://wikidocs.net/16045)

- `all()` : 모두 True여야 True 반환   /   `any()` : 하나라도 True인게 있으면 True

```python
cur = 3
temp = [1,3,6,2]
if any(cur<num for num in temp):
	print("There exist number that is larger than 3")
```

> any()는 특히 대소비교를 할 때 사용하면 sort보다 실행시간을 많이 줄일 수 있다.                     예를 들어 어떤 수와 어떤 리스트의 원소들을 비교하는데 해당 수가 리스트 안의 max값보다 큰지만 알고 싶다고 하자. 이 때, sort를 사용한 뒤 비교하면 리스트를 모두 정렬하기 때문에 시간이 걸린다. 하지만 any를 쓰면 리스트 내에 해당 수보다 큰 수가 있기만 하면 바로 True를 return하고 끝내기 때문에 시간이 덜 걸린다.
> 
- `chr()` : 아스키 코드표에서의 숫자를 문자   /   `ord()` : 문자를 아스키 코드표에서의 숫자

```python
print(chr(65))	# A
print(ord('A'))	# 65
```

- `dir(변수)` : 속성 목록 표현

- `dir()` : 인자 없이 사용할 경우 → 실행된 시점에서 유효한 변수 목록 표시
        
- `enumerate()` : 반복문 사용 시 몇 번째 반복문인지 확인할때

```python
>>> t = [1, 5, 7, 33, 39, 52]
>>> for p in enumerate(t):
...     print(p)
... 
(0, 1)
(1, 5)
(2, 7)
(3, 33)
(4, 39)
(5, 52)
```

```python
for i,letter in enumerate(['a', 'b', 'c'])
	print(i,letter)
0 a
1 b
2 c
```

인덱스를 1부터 시작하기

```python
for i,letter in enumerate(['a', 'b', 'c'],start=1)
	print(i,letter)
1 a
2 b
3 c
```

- `exec()` :  **문자열로 표현된 문을 인수로 받아** 파이썬 컴파일 코드로 변환

```python
>>>  a = 5
>>>  exec(‘ a = a + 4’)
>>> a
9
```

- `eval()` : **문자열로 표현된 파이썬 식을 인수로 받아** 파이썬 컴파일 코드로 변환

```python
>>>  a = 1
>>>  a = eval(‘a + 4’)
>>>  a
5
```

- `eval(expression)` : 매개변수로 받은 expression (=식)을 문자열로 받아서, 실행하는 함수

```python
# 파이썬 eval(expression) 예제
 
# 1. 문자열 덧셈
a = eval('"BlockDMask" + "blog"')
print(f"1. eval('\"BlockDMask\"' + '\" blog\"') : {a}")
 
# 2. 숫자 덧셈
b = eval("100 + 32")
print(f'2. eval("100 + 32") : {b}')
 
# 3. 내장 함수 abs
c = eval("abs(-56)")
print(f'3. eval("abs(-56)") : {c}')
 
# 4. 리스트 길이
d = eval("len([1,2,3,4])")
print(f'4. eval("len([1,2,3,4])") : {d}')
 
# 5. round 함수
e = eval("round(1.5)")
print(f'5. eval("round(1.5)") : {e}')
```

- `map(적용시킬함수, 적용할 요소들)`

```python
A,B = map(int,input().split()) #입력받으면서 바로 int형으로 바꿔서 넣어줌

if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')
```

- `lambda 매개변수들 : 식`

```python
target = [1, 2, 3, 4, 5]
result = map(lambda x : x+1, target)
print(list(result))
```

- `filter(적용시킬함수, 적용할 요소들)` : filter로 True만 걸러줌

```python
target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter(lambda x : x%2==0, target)
print(list(result))
...
[2, 4, 6, 8, 10]
```

- `len(데이터)` : 요소나 길이의 수 반환
- `max(데이터)` / `min(데이터)`
    
    알파벳 소문자 > 대문자 > 숫자
    
- `range(시작숫자, 종료숫자, step)`

파이썬에서 권장하지 않는 패턴

```python
>>> s = [1, 3, 5]
>>> for i in range(len(s)):
...     print(s[i])
... 
1
3
5
```

파이썬에서 권장하는 패턴

```python
>>> for v in s:
...     print(v)
... 
1
3
5
```

- `reversed(시퀀스)` : 역 iterator를 반환

```python
# for string
seq_string = 'Python'
print(list(reversed(seq_string)))
>>>['n', 'o', 'h', 't', 'y', 'P']

# for tuple
seq_tuple = ('P', 'y', 't', 'h', 'o', 'n')
print(list(reversed(seq_tuple)))
>>>['n', 'o', 'h', 't', 'y', 'P']

# for range
seq_range = range(5, 9)
print(list(reversed(seq_range)))
>>>[8, 7, 6, 5]

# for list
seq_list = [1, 2, 4, 3, 5]
print(list(reversed(seq_list)))
>>>> [5, 3, 4, 2, 1]
```

**string 객체로 리턴**

```python
stri = 'Python' #
reversedi=''.join(reversed(stri)) # .join() method merges all of the characters resulting from the reversed iteration into a new string
print(reversedi)
>>>nohtyP
```

```python
str="Python" 
stringlength=len(str) 
slicedString=str[::-1] # slicing 
print (slicedString) 
>>>nohtyP
```

### Extended slices

`arr[A:B:C]`의 의미는, index A 부터 index B 까지 C의 간격으로 배열을 만들어라

```python
>> arr = range(10) 
>> arr [0,1,2,3,4,5,6,7,8,9] 
>> arr[::2] # 처음부터 끝까지 두 칸 간격으로 [0,2,4,6,8] 
>> arr[1::2] # index 1 부터 끝까지 두 칸 간격으로 [1,3,5,7,9] 
>> arr[::-1] # 처음부터 끝까지 -1칸 간격으로 ( == 역순으로) [9,8,7,6,5,4,3,2,1,0] 
>> arr[::-2] # 처음부터 끝까지 -2칸 간격으로 ( == 역순, 두 칸 간격으로) [9,7,5,3,1] 
>> arr[3::-1] # index 3 부터 끝까지 -1칸 간격으로 ( == 역순으로) [3,2,1,0] 
>> arr[1:6:2] # index 1 부터 index 6 까지 두 칸 간격으로 [1,3,5]
```

- `round()`  : 반올림 해줌 예)  round(123.456 , 2) >> 123.46
- `sorted(데이터)` : 작은순부터 정렬하여 리스트형으로 반환!!!
- `sum()`  : 합
- `type(변수)` : 데이터 타입 반환
- `zip()`  :  튜플로 반환

```python
>>> numbers = [1, 2, 3]
>>> letters = ["A", "B", "C"]
>>> for pair in zip(numbers, letters):
...     print(pair)
...
(1, 'A')
(2, 'B')
(3, 'C')
```

```python
>>> for number, upper, lower in zip("12345", "ABCDE", "abcde"):
...     print(number, upper, lower)
...
1 A a
2 B b
3 C c
4 D d
5 E e
```

딕셔너리형으로 변환

```python
>>> keys = [1, 2, 3]
>>> values = ["A", "B", "C"]
>>> dict(zip(keys, values))
{1: 'A', 2: 'B', 3: 'C'}
```

 

### 데이터형

1. 숫자 자료형
- `int()` : 정수  / `float()` : 실수   / `complex()` : 복소수

복소수를 제외한 모든 숫자형은 아래의 연산 지원

| 연산 | 설명 |
| --- | --- |
| x + y | x와 y의 합 |
| x - y | x와 y의 차 |
| x * y | x와 y의 곱 |
| x / y | x와 y의 나눗셈 |
| x // y | x와 y의 정수 나눗셈 |
| x % y | x / y의 나머지 |
| -x | 음의 x |
| +x | x 그대로 |
| abs(x) | x의 절댓값 |
| int(x) | 정수로 변환된 x |
| float(x) | 실수로 변환된 x |
| complex(real, imag) | real + imag*1j 값을 갖는 복소수 |
| c.conjugate() | 복소수 c의 켤레 |
| divmod(x, y) | (x//y, x%y)의 튜플 |
| pow(x, y) 또는 x**y | x의 y 거듭제곱 |
1. 논리형
- `bool()`  : True , False

None, False
숫자 형들의 영: 0, 0.0, 0j, Decimal(0), Fraction(0, x) 등
빈 시퀀스, 컬렉션: '', (), [], {}, set(), range(0) 등

1. 데이터 
- `str()` : 문자열로 변환
- `char()` : 문자로 변환
- `dict()`
- `set()`
- `list()`
- `tuple()`

```python
>>> range(5,10)
range(5, 10)
>>> list(range(5,10))
[5, 6, 7, 8, 9]
>>> tuple(range(5,10))
(5, 6, 7, 8, 9)
```

### 입력과 출력

- `print()` : 출력
- `format()`  :  '{인덱스0}, {인덱스1}'.format(값0, 값1)
- `print(f’프린트할 내용 {변수}’)` f-string 포매팅
    
    ```python
    print(f'Case #{i}: {a+b}') # i랑 a+b의 변수만 바꿔서 출력할 수 있음
    ```
    
- `input()`  : 입력 → 숫자데이터를 받아도 문자열형으로 저장됨

```python
data = input('숫자 입력하시오: ')
```

입력을 1개 이상 받을 때 

`split(기준문자)` : 기준문자를 기준으로 하여 문자열을 나눔 

```python
data1, data2 = input('숫자 입력하시오: ').split() #공백으로 분리
```

- **`sys.stdin.readline()` → input 대신 사용**

```python
import sys
a,b,c = map(int,sys.stdin.readline().split())
```

[[Python 문법] 파이썬 입력 받기(sys.stdin.readline)](https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline)

- 아스키코드 변환

`ord(’문자열’)` : 아스키코드 숫자

`chr(아스키코드 숫자)` : 아스키코드가 의미하는 문자

- 데이터형 변환
1. `int()` : 정수로 변환
2. `float()` : 실수로 변환
3. `str()` : 문자열로 변환
4. `char()` : 문자로 변환
5. `bool()`
