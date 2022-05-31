# C언어 TIL

- 출력

```c
printf(%d , 100);
```

- 입력

```c
scanf(%d , 100);
```

| %d, %x, %o | 정수 (10진수, 16진수, 8진수) |
| --- | --- |
| %f, %lf | 실수 |
| %c | 문자 (한글자만 ‘ ‘) |
| %s | 문자열 (한글자 이상 “ ”) |
- 서식문자

| \n | 다음줄로 이동 |
| --- | --- |
| \t | 탭 |
| \\ | \ 출력 |
| \’ | ‘ 출력 |
| \” | “ 출력 |
- 데이터형식

8bit = 1byte

| short | 작은 정수형 | unsigned short | (-)부호없는 | 2byte |
| --- | --- | --- | --- | --- |
| int | 정수형 | unsigned int | (-)부호없는 | 4byte |
| long | 큰 정수형 | unsigned long | (-)부호없는 | 4byte |
| float | 실수형 |             - |  | 4byte |
| double | 큰 실수형 |             - |  | 8byte |
| long double | 큰 실수형 |             - |  | 8byte |
| char | 문자형 또는 정수형 | unsigned char | (-)부호없는 | 1byte |

`sizeof()` : 데이터형의 크기 확인

char형 서식에 따라 달라짐

```c
char a;
a = 'A';
printf(" %c\n", a);          // %앞에 한칸 띄어주기
printf(" %d\n", a);
```

결과

>> a

>> 65

A의 아스키코드 10진수로 65이기 때문!

- 문자열

= 문자형 집합 

무자형 데이터 형식 char 는 한글자만 저장가능하므로 문자열은 한문자가 여러개 이어진 것과 같음

```c
char str[10];

strcpy(str, "Hello")
```

`strcpy()` : 다른 데이터 형식의 대입 연산자(=)와 같음

0~9까지중에 0~4까지 자리가 차고 5자리에는 널(null)문자가 들어감 

| str[0] | str[1] | str[2] | str[3] | str[4] | str[5] | str[6] | str[7] | str[8] | str[9] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| H | e | l | l | o | \0 |  |  |  |  |

널문자(\0)는 문자열의 끝을 알려줌

- 연산자

사칙연산이랑 대입연산자 생략

1. 증감연산자

| 연산자 | 예 | 설명 |
| --- | --- | --- |
| ++ | a++ | a = a+1 |
| -- | a-- | a = a-1 |
1. 관계연산자

| 연산자 | 의미 |
| --- | --- |
| == | 같다 |
| != | 같지않다 |
| > | 크다 |
| < | 작다 |
| >= | 크거나 같다 |
| <= | 작거나 크다 |
1. 논리연산자

| 연산자 | 의미 |
| --- | --- |
| && | 그리고(AND) |
| || | 또는(OR) |
| ! | 부정(NOT) |
1. 비트연산자 (생략)

- 연산자 우선순위
1. 괄호가 최우선
2. 곱셈/나눗셈 → 덧셈/뺄셈 
3. 대입이 가장 마지막!

- if문

```cpp
if (조건식) {
실행할 문장 1;
}
else if (조건식) {
실행할 문장 2;
}
else {
실행할 문장 3;
}
```

- for문

```cpp
for(초깃값; 조건식; 증감식) {
반복 실행할 문장;
}
```

- while문

```cpp
while(조건식) {
반복 실행할 문장;
}
```

`break`문 → 무조건 반복문(for,while) 블록 밖으로 탈출

`continue`문 → 무조건 블록끝으로 건너뛴 후 다시 반복문 처음으로 돌아감

- 배열

- 배열의 초기화

`int aa[4] = {100, 200, 300, 400}`

- 배열의 크기

배열의 크기(요소의 개수) = `sizeof(aa) / sizeof(int);`

# C pointer

```c
#include <stdio.h>

int swap (int* num1, int* num2){
  
    int temp;
 
    temp = *num1;
    *num1 = *num2;
    *num2 = temp;
 
    return 0;
}

int main(){

   int a = 5;
   int b = 10;

   printf("a = %d /n b = %d", a, b);

   swap(&a, &b);

   printf("a = %d /n b = %d", a, b);

}
```

```c
#include <stdio.h>

int main(){

    char arr[6] = {"hello"};

    char* ptr;
    ptr = &arr[0];

    printf("%c", ptr[1]);
    //이거랑 같음
    printf("%c", *(ptr+1)); 

    return 0;
}
```