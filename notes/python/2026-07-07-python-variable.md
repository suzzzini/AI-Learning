# Python이란?
Python은 사람이 이해하기 쉬운 문법을 가진 고급 프로그래밍 언어이다.

1991년 Guido van Rossum이 개발했으며,
현재는 웹 개발, 데이터 분석, 인공지능, 자동화, 보안 등 다양한 분야에서 가장 많이 사용되는 언어 중 하나이다.

## Python 특징
- 문법이 간단
- 다양한 라이브러리 제공
- 여러 운영체제에서 사용 가능

## 왜 AI에서 Python을 사용하는가?
AI 모델은 대부분 복잡한 수학 계산과 대량의 데이터 처리가 필요하다.
Python은 이러한 작업을 쉽게 할 수 있도록 이미 만들어진 라이브러리가 매우 많다.

예를 들어,
| 라이브러리        | 용도             |
| ------------ | -------------- |
| NumPy        | 행렬 및 수학 계산     |
| Pandas       | 데이터 분석         |
| Matplotlib   | 데이터 시각화        |
| scikit-learn | 머신러닝           |
| PyTorch      | 딥러닝            |
| TensorFlow   | 딥러닝            |
| OpenAI SDK   | ChatGPT API 사용 |

즉, Python은 AI를 쉽고 빠르게 개발할 수 있도록 도와주는 언어라고 이해하면 된다.


## Python은 인터프리터 언어란?
프로그래밍 언어는 크게 두 가지 방식으로 실행된다.

### 컴파일언어 (C, C++)
- 프로그램 전체를 한 번에 번역한 후 실행한다.
``` text
소스코드
    ↓
컴파일
    ↓
실행 파일(.exe)
    ↓
실행
```
- 장점
  - 실행 속도가 빠름
- 단점
  - 수정할 때마다 다시 컴파일 필요
  - 
### 인터프리터 언어 (Python)
- 한 줄씩 해석하며 실행

``` text
소스코드
    ↓
Python Interpreter
    ↓
한 줄씩 해석하며 실행
```
- 장점
  - 개발이 빠름
  - 테스트에 용이
- 단점
  - 컴파일 언어보다 실행속도가 느림

Python은 내부적으로는 소스 코드를 바이트코드(bytecode)로 변환한 뒤, Python Virtual Machine(PVM)이 이를 실행하는 구조다.
지금 단계에서는 "인터프리터가 코드를 실행해준다" 정도로 이해하면 된다.

## Python 실행 과정
(1) 코드 작성
 print("Hello")
(2) 코드 실행 시 
``` text
① Python 코드 작성
        ↓
② Python Interpreter 실행
        ↓
③ Python 코드를 Bytecode로 변환
        ↓
④ Python Virtual Machine(PVM)이 Bytecode 실행
        ↓
⑤ 운영체제(macOS, Linux, Windows)에 요청
        ↓
⑥ CPU가 명령을 수행
        ↓
⑦ 화면에 Hello 출력
``` 

# 변수
컴퓨터는 계산하거나 처리할 데이터를 어딘가에 저장해야 한다.
에를 들어 차량의 현재 속도를 저장할 때,
speed = 100

변수가 없다면, 현재 속도를 기억할 방법이 없다.
즉, 변수는 데이터를 저장하고, 나중에 다시 사용할 수 있도록 해주는 이름표 역할을 한다.

## 변수 이름 규칙
아래와 같은 Python 변수는 불가하다
- 숫자로 시작 : 1speed
- '-' 사용 : my-name
- 예약어 : def, class 등

## 변수 선언  
 speed = 100

 speed 라는 이름으로 100이라는 값을 참조하도록 한다.
 라는 의미이며, 

 실제로는 Python이 메모리 100이라는 객체를 만들고,
 speed 라는 이름이 그 객체를 가리키는 구조다.
 
 ## 변수 저장 공간
 프로그램이 실행되면 필요한 데이터는 RAM(메모리)에 저장된다.
 변수는 RAM 어딘가에 저장됨 (week3에서 공부 예정)

# 자료형
자료형(Data Type)은 변수에 어떤 종류의 데이터를 저장하는지 나타내는 정보이다.

| 자료형   | 설명   | 예시    |
| ----- | ---- | ----- |
| int   | 정수   | 100   |
| float | 실수   | 3.14  |
| str   | 문자열  | "ABC" |
| bool  | 참/거짓 | True  |

## int
    speed = 100
## float
    temperature = 36.5
## str
    model = "IONIQ5"
## bool
    is_safe=True
## type()
    print(type(speed))
    변수의 자료형을 확인하는 함수

# 실습
01_vehicle_info_print.py

# 이해한 내용
## Python 코드 작성시 Main 의 필요성
- main 함수가 없어도 됨
``` code
name = "Laura"
age = 30
company = "ABC"

print(name)
print(age)
print(company)
``` 
- 다만 실무에서는 아래와 같이 작성
``` code
def main():
    name = "Laura"
    age = 30
    company = "ABC"

    print(name)
    print(age)
    print(company)

if __name__=="__main__":
    main()
``` 
* 아래는 이 파일을 직접 실행했을 때만 main()을 실행하라는 의미
    if __name__=="__main__":
        main()

* 이렇게 작성하는 이유 : 
  * 프로젝트 구조
    ``` text
    AI-Learning/
    ├── main.py
    └── utils.py
    ```
  * main 코드
    ``` text
    import utils
    print(utils.add(3, 5))
    ``` 
  * utils 코드
    ```text
    def add(a, b):
        return a + b

    def main():
        print("utils 테스트")

    if __name__ == "__main__":
        main()
    ```
-> main에서 utils 내부 함수를 호출할 때, utils 에 있는 main 을 실행하지 않음


# 아직 궁금한 것
Python은 왜 실행 속도가 C보다 느릴까?
- C는 컴파일러가 기계어(0,1)로 변환하여 CPU가 바로 실행
- Python은 인터프리터가 바이트코드로 변환하고, PVM이 CPU에 전송하여 실행
RAM에는 변수 말고 또 무엇이 저장될까?
- 프로그램이 실행되는 동안 필요한 모든 것을 저장
  - 프로그램코드
  - 변수
  - 값
  - 함수
  - print 함수
  - python 자체
  - 운영체제정보
Python은 메모리를 자동으로 어떻게 관리할까?
- C의 경우 malloc, free 로 메모리 할당/해제를 해줘야 함
- Python은 GC(Garbage Collector)가 자동으로 해줌
100과 "100"은 메모리에서 어떻게 다르게 저장될까?
- 100: 숫자 100으로 저장
- "100": [1] [0] [0] 처럼 문자 하나하나가 저장됨

# 이해도 체크

Q1.
Python이 AI 분야에서 가장 많이 사용되는 이유는 무엇인가?
- 다양한 라이브러리를 제공하고 있기에 AI 모델을 단 몇 줄의 코드로 실행 가능하다.
- 
Q2.
컴파일 언어와 인터프리터 언어의 가장 큰 차이는 무엇인가?
- 컴파일 언어는 전체 코드를 한번에 기계어로 변환하여 실행하며, 인터프리터 언어는 실행 시 인터프리터가 코드를 해석하며 실행한다.

Q3.
다음 코드에서 speed의 자료형은 무엇인가?
speed = "100"
- str

Q4. 
왜 100과 "100"은 서로 다른 값으로 취급될까?
- 100은 int type이며, "100"은 string 타입이기 때문이다.
- 컴퓨터는 숫자와 문자열을 메모리에 저장하는 방식과 사용할 수 있는 연산이 서로 다르기 때문에 서로 다른 값으로 취급한다.