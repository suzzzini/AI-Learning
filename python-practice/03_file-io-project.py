""" 
03_file-io-project.py

Project 1
    vehicle.log 파일을 읽어서 화면에 출력하기.
Project 2
    ERROR가 포함된 줄만 출력하기.
Project 3
    INFO, WARNING, ERROR의 개수를 세기.
    예시>
    INFO : 10
    WARNING : 2
    ERROR : 1
Project 4
    사용자가 검색어를 입력하면 해당 문자열이 포함된 로그만 출력하기.
    예시>
    검색어 : CAN
    ↓
    ERROR CAN IDS Alert
"""

def project1():
    with open("datasets/vehicle.log","r") as file:
        data = file.read()
    print(data)

def project2():
    with open("datasets/vehicle.log","r") as file:
        for line in file:
            if "ERROR" in line:
                print(line)
def project3():
    with open("datasets/vehicle.log","r") as file:
        cnt_info = 0
        cnt_warning = 0
        cnt_error = 0
        for line in file:
            if line.startswith("INFO"):
                cnt_info += 1
            elif line.startswith("WARNING"):
                cnt_warning += 1
            elif line.startswith("ERROR"):
                cnt_error += 1
            """
            # INFO Previous ERROR has been cleared 와 같은 코드 커버 불가
            if "ERROR" in line:
                cnt_error +=1
            if "INFO" in line:
                cnt_info +=1
            if "WARNING" in line:
                cnt_warning +=1
            """
    print(f"INFO : {cnt_info}")
    print(f"WARNING : {cnt_warning}")
    print(f"ERROR : {cnt_error}")


def project4():
    search =input("검색어: ")
    cnt=0
    with open("datasets/vehicle.log","r") as file:
        for line in file:
            if search in line:
                cnt+=1
                print(f"[{cnt}] {line.strip()}")
    if cnt == 0:
        print("검색 결과가 없습니다.")
    else:
        print(f"총 {cnt}건 검색되었습니다.")

def main():
    project4()

if __name__=="__main__":
    main()