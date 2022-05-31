# C++ TIL

# Chapter2

```cpp
#include <iostream>
using namespace std;

/* std사용하는 경우
int main() {
	std::cout << "Hello\n";
	std::cout << "첫번째 맛보기입니다.";
	return 0;
}
*/

// using namespace std;를 사용하면 std:: 쓰지 않아도됨
int main() {
	cout << "Hello\n";
	cout << "첫번째 맛보기입니다.";
	return 0;
}
```

- 주석문
1. `/* */` : 문단 전체 주석
2. `//` : 한줄 주석

- main()함수

```cpp
int main() {
	..............
	return 0;  // 필요에 따라 0이 아닌 다른 값을 리턴할 수 있음
} // 요새 C++에서는 return 0; 생략해도 됨
```

```cpp
void main() {
	..............
}  // return이 필요없음! 표준은 아님

```

- 출력
1. `cout`

```cpp
std::cout << "Hello\n";
```

```cpp
using namespace std;

cout << "Hello\n";
```

 2. `<<`

\n 또는 endl 사용해서 출력을 다음줄로 이동

```cpp
std::cout << "Hello" << '\n';
std::cout << "Hello" << std::endl;;
```

```cpp
using namespace std;

cout << "Hello" << '\n';
cout << "Hello" << endl;;
```

- 입력

```cpp
int width;
cin >> width;
```

width라는 변수를 선언해주고 사용자가 입력하는 값을 width로 받아옴

**문자열 다루기1 - C-스트링**

- `cin.getline()` : 공백이 포함된 문자열을 입력받을 수 있음

`cin.getline(char buf[] , int size, char delimitChar)`

`buf` : 키보드로부터 읽은 문자열을 저장할 배열

`size` : buf[]의 배열 크기

`delimitChar` : 문자열 입력 끝을 지정하는 문자 → 안쓰면 디폴트값이 \n

최대 size-1 개의 문자를 입력받거나  delimitChar 로 지정된 문자 만나면 문자열 입력 종료 

`#include <cstring>`

`strcpy()`  : 문자열 복사

`strcmp()`  : 두 문자열 비교

`strlen()`  : 문자열의 길이

- 공백문자

빈칸, \t , \n , \r , \f , \v

`int isspace(char c)` : c가 공백 문자이면 true 리턴

**문자열 다루기1 - string 클래스**

```cpp
#include <string>

string song("Falling in love with you");
string elvis("Elvis Presley");
string singer;
```

# Chapter 3

클래스 선언부

```cpp
class Circle {
public:
   int radius;          // 멤버 변수
   double getArea();    // 멤버 함수의 원형

};  //반드시 세미콜론
```

클래스 구현부 → 멤버 함수의 코드 구현

```cpp
double Circle::getArea() {      //범위지정연산자(::)를 사용해서 클래스이름과 멤버함수 기술
       return 3.14*radius*radius;

}
```

객체

```cpp
int main() {
	Circle donut;
	donut.radius = 1;  //public 이니까 가능
	double area = donut.getArea();  // getArea() 리턴값이 area에 저장
	cout << "donut 면적은 " << area << endl;

	Circle pizza;
	pizza.radius = 30;  
	area = pizza.getArea();
	cout << "donut 면적은 " << area << endl;
}
```

- 객체 멤버 접근

`donut.radius = 1;` : 객체이름.멤버

- 생성자 : 특별한 멤버 함수를 통해 객체 초기화

클래스 선언부에 생성자

```cpp
class Circle {
public:
	int radius;
	Circle();           // 기본 생성자
	Circle(int r);      // 매개 변수 있는 생성자
	double getArea();
};
```

생성자 구현?

```cpp
Circle::Circle() {
	radius = 1;
	cout << "반지름 " << radius << "인 원 생성" << endl;
}

Circle::Circle(int r) {
	radius = r;
	cout << "반지름 " << radius << "인 원 생성" << endl;
}
```

- 위임 생성자

```cpp
Circle::Circle() :Circle(1) {} // 위임 생성자

Circle::Circle(int r) {        // 타켓 생성자
	radius = r;
	cout << "반지름 " << radius << "인 원 생성" << endl;
}
```

- 클래스의 멤버 변수 초기화
1. 생성자 코드에서 멤버 변수 초기화

```cpp
class Point {
   int x, y;
public :
   Point();
   Point(int a, int b);
};

//생성자
Point::Point() {x=1; y=0;}
Point::Point(int a , int b) {x=a; y=b}
```

1. 생성자 서두에 초깃값으로 초기화

```cpp
class Point {
   int x, y;
public :
   Point();
   Point(int a, int b);
};

//생성자
Point::Point() : x(0) , y(0) {}
Point::Point(int a , int b) : x(a), y(b) {}
```

1. 클래스 선언부에서 직접 초기화

```cpp
class Point {
   int x = 0, y = 0;
   . . .
};
```

- 기본 생성자 = 디폴트 생성자 → 매개변수 없는 생성자

- 소멸자

```cpp
class Circle {
public:
	int radius;
	Circle();           // 기본 생성자
	Circle(int r);      // 매개 변수 있는 생성자
	
  ~Circle();  // 소멸자
};
```

하나만 존재하며 리턴타입 없고 매개변수도 없다

```cpp
Circle::~Circle() {}
```

목적 : 객체가 사라질 때 필요한 마무리 작업

(동적으로 할당받은 메모리 돌려주기, 열어 놓은 파일 정저장하고 닫기와 같은)

- 지역 객체와 전역 객체

- 접근 지정자
1. private    → 디폴트값
2. public
3. protected

멤버 변수는 private으로 지정하는 것이 바람직함

# Chapter 4

- 객체 포인터

```cpp
Circle donut;
Circle *p;  // 포인터 선언

p = &donut;  // 포인터에 객체 주소 저장
d = p->getArea();  // 멤버 함수 호출
// d = donut.getArea() 이렇게 안씀
```

```cpp
#include <iostream>
using namespace std;

class Circle{
int radius; //private

public:
Circle() {radius = 1;}
Circle(int r) {radius = r;}
double getArea();
};

double Circle::getArea(){
return 3.14*radius*radius;
}

int main(){

Circle donut;
Circle pizza(30);

// 객체 이름으로
cout<< donut.getArea() <<endl;

// 객체 포인터로
Circle *p;
p = &donut;
cout << p->getArea() << endl;
cout<< (*p).getArea() <<endl;

p = &pizza;
cout << p->getArea() << endl;
cout<< (*p).getArea() <<endl;
```

- 객체 배열

```cpp
#include <iostream>
using namespace std;

class Circle{
int radius; //private

public:
Circle() {radius = 1;}
Circle(int r) {radius = r;}
void setRadius(int r) {radius = r;}
double getArea();
};

double Circle::getArea(){
return 3.14*radius*radius;
}

int main(){

Circle circleArray[3];

circleArray[0].setRadius(10);
circleArray[1].setRadius(20);
circleArray[2].setRadius(30);

for(int i=0; i<3; i++)
cout << "Circle" << i << "의 면적은" << circleArray[i].getArea() << endl;

Circle *p;
p = circleArray;
for(int i=0; i<3; i++)
cout << "Circle" << i << "의 면적은" << p->getArea() << endl;
p++;
}
}
```

- 객체 배열 초기화

`Circle cicleArray[3] = { Circle(10), Circle(20), Circle() };`

circleArray[0] 은 10으로

circleArray[1] 은 20으로

circleArray[2]은 기본 생성자를 호출하여 1로 

- 동적메모리 할당

     - new와 delete 연산자

기본형식

```cpp
int *p = new int;  // 데이터 타입 *포인터 변수 = new 데이터 타입;
delete p;          // delete 포인터변수;

int *pCircle = new Circle(); 
delete pCircle;
```

힙 메모리가 부족하면 new는 NULL을 반환하므로 미리 체크하기

```cpp
if(!p){
return;
}
```

- 배열의 동적 할당

```cpp
int *p = new int [5];  // 데이터타입 *포인터변수 = new 데이터타입 [배열의 크기]
delete [] p;  // delete [] 포인터변수;
```

배열에 순서대로 기록

```cpp
for(int i=0; i<5; i++)
p[i] = i;  // *(p+i) = i; 와 같음

```

배열을 동적할당 받을때 생성자를 통해 직접 초기화할 수 없음!

하지만 이건 가능 → 1, 2, 3, 4로 초기화된 정수 배열 생성

`int *p = new int [] {1, 2, 3, 4}`

- 객체의 동적 생성 및 반환

```cpp
// 1. 기본생성자 호출 경우
int *p = new Circle;   // 클래스 이름 *포인터 변수 = new 클래스 이름;
int *p = new Circle(); // -> 위아래 같음 (원래 객체 생성할때는 '()' 안붙임) 
delete p;                // delete 포인터변수;

// 2. 생성자 Circle(30) 호출 경우
int *q = new Circle(30); // 클래스 이름 *포인터 변수 = new 클래스 이름(생성자매개변수리스트);
delete q;                // delete 포인터변수;

```

---

### 객체 배열의 사용 (헷갈리지 말기!)

1. 객체 배열처럼 사용하기

```cpp
Circle *pArray = new Circle[3];
pArray[0].setRadius(10);
pArray[1].setRadius(20);
pArray[2].setRadius(30);

for(int i=0; i<3;i++) {
cout << pArray[i].getArea();
```

1. 포인터로 사용하기

```cpp
Circle *pArray = new Circle[3];
pArray->setRadius(10);
(pArray+1)->setRadius(20);
(pArray+2)->setRadius(30);

for(int i=0; i<3;i++) {
cout << (pArray+i)->getArea();
```

- this 포인터

멤버변수 이름이랑 매개변수 이름 같게 할 때 사용

- string 클래스

```cpp
#include <string>   // 맨앞에 string 클래스 헤더파일 선언해줘야함!

//생성자를 이용하여 객체 생성하는 방법
string str;
string address("우연이집");
string copyAddress(address);

char text[] = { 'L','o','v','e',' ','C','+','+','\0' };
string title(text);
```

- 공백을 포함한 문자열을 입력받을때

`getline` 함수 

```cpp
string name;
getline(cin, name, '\n'); //(cin, 객체이름, 문자열의 마지막을 표시하는 구분문자)
```

- string 함수
1. `compare()` : 문자열 비교 → ==,<,>

문자열과 str을 비교하여 같으면 0

/ str보다 사전순으로 앞에 오면(-)  

/ 뒤에  오면 (+)

```cpp
string name = "Kitae";
string str = "Kito";

int res = name.compare(str);
if(res==0) cout<<"같다";
else if(res<0) cout<<name<< "<" <<str; // 결과 
else cout <<str << "<" << name;
```

비교 연산자를 쓰는 경우

```cpp
if(name == str) cout<<"같다";
if(name < str) cout<< name<<"이"<<str<<"보다 사전에서 먼저 나옴";
```

1. `append()`  : 문자열 연결 → +

```cpp
string a("I");
a.append(" love ");
```

덧셈연산자를 쓰는경우

```cpp
string a("I love");
string c(" you");
string c;
c = a+b;
```

1. `insert()`  : 문자열 삽입

```cpp
string a("I love you");
a.insert(2, "really"); //2 위치에 삽입하기
```

1. `replace()`  : 문자열 대치

```cpp
string a("I love you");
a.replace(2, 4, "like");  //2위치부터 4개의 문자를(love) like로 바꿈
```

1. 문자열 길이  → 매개변수 X

- `length()`  : 문자열 길이

- `size()`  : 문자열 길이 → lenght와 동일한 결과

- `capacity()`  : 객체 내부 메모리 용량

1.  문자열 삭제 

- `erase()`  : 문자열 일부 삭제

- `clear()`  : 문자열 전체 삭제 → 매개변수 X

```cpp
string a("I love you");
a.erase(0,7); //0위치부터 7개의 문자 삭제 -> you로 변경
a.clear();
```

1. `substr()`  : 서브스트링

문자열에서 일부분을 발췌한 문자열(서브스트링)을 얻을 수 있음

```cpp
string a("I love you");
string b = a.substr(2,4); //2위치부터 4개의 문자 발췌 -> love
string c = a.substr(2); //2부터 끝까지 -> love you
```

1. `find()` : 문자열 검색

문자열에서 특정 문자나 문자열을 발견하면 첫 번째 인덱스를 리턴

발견하지 못하면 -1

```cpp
string a = "I love love you";
int index = a.find("love"); // -> 인덱스 2리턴
index = a.find("love", index+3); //-> 3위치에서 부터 love검색해서 7리턴
```

1. 문자열의 각 문자 다루기

```cpp
string a("I love you");
char ch1 = a.at(7); //y
char ch2 = a[7];  //y
a[7] = "t"; // I love tou
```

1. `stoi()`  : 문자열의 숫자 변환

```cpp
string year = "2022";
int n = stoi(year);
```

1. 문자 다루기

```cpp
#include <locale>

string a = "hello"
for(int i =0; i<a.lenght; i++) a[i] = toupper(a[i]);  //HELLO

if(isdigit(a[0])) cout<<"숫자";
else if(isalpha(a[0])) cout<<"문자"; //결과
```