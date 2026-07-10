'''
속도 > 100
→ 과속입니다.

배터리 < 20
→ 배터리가 부족합니다.

둘 다 해당
→ 과속이며 배터리가 부족합니다.

둘 다 아니면
→ 정상 운행 중입니다.

'''
def check_highspeed(speed):
    return speed > 100
        
def check_lowbattery(battery):
    return battery < 20

def check_vehicle(speed, battery):
    if check_highspeed(speed) and check_lowbattery(battery):
        return "과속이며 배터리가 부족합니다."
    elif check_lowbattery(battery):
        return "배터리가 부족합니다."
    elif check_highspeed(speed):
        return "과속입니다."
    
    return "정상 운행 중입니다."

def check_score(speed, battery):
    score = 0

    if speed >= 120:
        score += 50
    elif speed >= 100:
        score += 20

    if battery < 10 : 
        score += 50
    elif battery < 20 :
        score += 30

    return score

def print_risk_score (score):
    if score >= 70:
        print("High Risk")
    elif score >=30:
        print("MEDIUM RISK")
    else:
        print("LOW RISK")

def main():
    print("=========================")
    print("Vehicle Inspection Result")
    print("=========================")
    num_vehicle= int(input("총 검사할 차량 수 : "))

    for i in range(num_vehicle):
        print(f"\n==== Vehicle {i+1} ====")
        vehicle = input("Vehicle : ")
        speed = int(input("Speed(km/h): "))
        battery = int(input("Battery(%): "))

        status = check_vehicle(speed, battery)
        print(status)
        score = check_score(speed, battery)
        print_risk_score(score)

if __name__ == "__main__":
    main()
