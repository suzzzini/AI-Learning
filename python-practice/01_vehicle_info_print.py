# python 실습
## 변수
### speed = 100

## 데이터 출력
### print(speed)
### print(f"Speed = {speed}")
### print("speed",speed)

## 데이터 입력받기
### name = input("이름 입력 : ")

# 차량 정보 출력하는 프로그램

model = input("모델 입력 : ")
speed = int(input("속도(km/h) 입력 : "))
battery = int(input("배터리(%) 입력 : "))
ready = input("상태 입력 : ")

print(type(speed), type(battery))
print("Vehicle Information")
print(f"Model : {model}")
print(f"Speed : {speed} km/h")
print(f"Battery : {battery} %")
print(f"Ready : {ready}")

