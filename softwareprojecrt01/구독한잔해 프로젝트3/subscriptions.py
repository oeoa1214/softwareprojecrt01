subscriptions = {}
import json
import os
from datetime import datetime
import winsound
#OS os는 파일이나 폴더 위치를 다룰 때 쓰는 Python 기본 기능
#JSON 파일의 정확한 위치를 만들어 둠
#__file__은 현재 실행 중인 subscriptions.py 파일 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "subscriptions.json")
#구독 등록
def register_subscription():
    print("===== 구독 등록 =====")

    # 서비스명 중복 예외
    while True:
        service_name = input("서비스명을 입력해주세요: ")
        if service_name.strip() == "":
            print("서비스명을 입력해주세요.")
            continue
  
        if service_name in subscriptions:
            print("이미 등록된 서비스입니다. 다른 서비스명을 입력해주세요.")
        else:
            break

    # 요금 예외
    while True:
        cost = input("요금을 입력해주세요:")

        try:
            cost = float(cost)
        except ValueError:
            print("요금은 숫자로 입력해주세요.")
            continue

        if cost < 0:
            print("요금은 0 이상의 숫자로 입력해주세요.")
            continue

        break

    # 결제 주기 예외
    while True:
        cycle = input("결제 주기를 입력해주세요. (월간/연간/4주):")

        if cycle == "월간" or cycle == "연간" or cycle == "4주":
            break
        else:
            print("결제 주기는 월간, 연간, 4주 중 하나를 입력해주세요.")

    # 다음 결제 예정일
    while True:
        next_payment = input("다음 결제 예정일을 입력해주세요. (YYYY-MM-DD):")

        try:
            datetime.strptime(next_payment, "%Y-%m-%d")
            break
        except ValueError:
            print("날짜는 YYYY-MM-DD 형식의 실제 존재하는 날짜로 입력해주세요.")

    category = input("카테고리를 입력해주세요:")

    # 마지막 이용일
    while True:
        last_used = input("마지막 이용일을 입력해주세요. (YYYY-MM-DD): ")

        try:
            datetime.strptime(last_used, "%Y-%m-%d")
            break
        except ValueError:
            print("날짜는 YYYY-MM-DD 형식의 실제 존재하는 날짜로 입력해주세요.")

    # 무료체험 종료일
    while True:
        trial_end = input("무료체험 종료일을 입력해주세요. (없으면 Enter):")

        if trial_end == "":
            trial_end = None
            break

        try:
            datetime.strptime(trial_end, "%Y-%m-%d")
            break
        except ValueError:
            print("날짜는 YYYY-MM-DD 형식의 실제 존재하는 날짜로 입력해주세요.")

    while True:
        shared_count = input("공유 인원수를 입력해주세요. (혼자 사용 시 1):")

        try:
            shared_count = int(shared_count)
        except ValueError:
            print("공유 인원수는 1 이상의 정수로 입력해주세요.")
            continue

        if shared_count <= 0:
            print("공유 인원수는 1 이상의 정수로 입력해주세요.")
            continue

        break

    subscriptions[service_name] = {
        "cost": cost,
        "cycle": cycle,
        "next_payment": next_payment,
        "category": category,
        "last_used": last_used,
        "trial_end": trial_end,
        "shared_count": shared_count
    }

    print(f"{service_name}가 등록되었습니다.")


#구독 조회
def view_subscriptions():
    if not subscriptions:
        print("등록된 구독이 없습니다.")
        return

    print("===== 구독 조회 =====")

    for key, value in subscriptions.items():
        print("서비스명:", key)
        print(f"요금: {float(value['cost']):,.2f}원")
        print(f"결제 주기: {value['cycle']}")
        print(f"다음 결제 예정일: {value['next_payment']}")
        print(f"카테고리: {value['category']}")
        print("--------------------")

    detect_cancellation_candidates()


#구독 삭제
#만약 구독이 존재하지 않으면 "해당 서비스가 존재하지 않습니다." 출력
def delete_subscription():
    print("===== 구독 삭제 =====")
    service_name = input("삭제할 서비스명을 입력해주세요: ")
    if service_name in subscriptions:
        del subscriptions[service_name]
        print(f"{service_name} 구독이 삭제되었습니다.")
    else:
        print("해당 서비스가 존재하지 않습니다.")


#구독 저장
#open() 함수를 사용하여 subscriptions.json 파일을 쓰기 모드로 연다. encoding="utf-8" 옵션을 사용하여 한글이 깨지지 않도록 합니다.
#json.dump() 함수를 사용하여 subscriptions 딕셔너리를 JSON 형식으로 저장합니다.
#ensure_ascii=False 옵션을 사용하여 한글이 깨지지 않도록 하고, indent=4 옵션을 사용하여 JSON 파일을 보기 좋게 들여쓰기합니다.
#with 블록이 끝나면 파일이 자동으로 닫히게 해주는 예약어
def save_subscriptions():
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(subscriptions, file, ensure_ascii=False, indent=4)
       # 저장 완료 효과음 - 빠밤카팜 느낌
    winsound.Beep(800, 70)
    winsound.Beep(1050, 90)
    winsound.Beep(1350, 70)
    winsound.Beep(1750, 180)

    print("구독 정보를 JSON 파일에 저장했습니다.")
    print("이용해주셔서 감사합니다~")


#구독 취소 후보 탐지 함수 로직
#현재 날짜 - last_used > 30일→ 해지 후보
#무료체험 일자 - 현재 날짜→ 양수면 D-n 0이면 D-day 음수면 무료체험 종료
def detect_cancellation_candidates():

    current_date = datetime.now().date()

    candidate_found = False

    # 해지 후보 검사
    for key, value in subscriptions.items():
        last_used = datetime.strptime(
            value["last_used"],
            "%Y-%m-%d"
        ).date()

        days_passed = (current_date - last_used).days
        #30일 이상 경과한 경우 해지 후보로 출력
        if days_passed > 30:
            if not candidate_found:
                print("===== 해지 후보 =====")

            print(f"{key} - 마지막 이용 후 {days_passed}일 경과")
            candidate_found = True

    # 모든 구독을 다 확인한 뒤 실행
    # 설계서에는 없지만 추가 했습니다.
    if not candidate_found:
        print("해지 후보가 없습니다.")

    # 무료체험 종료일 검사
    for key, value in subscriptions.items():

        if value["trial_end"]:

            trial_end = datetime.strptime(
                value["trial_end"],
                "%Y-%m-%d"
            ).date()

            days_left = (trial_end - current_date).days

            if days_left > 0:
                print(f"{key} - 무료체험 종료 D-{days_left}")

            elif days_left == 0:
                print(f"{key} - 무료체험 종료 D-day")

            else:
                print(f"{key} - 무료체험이 종료되었습니다.")


#구독 불러오기 함수
def load_subscriptions():
    #3. JSON 파일이 없으면 그냥 넘어가게 함
    if not os.path.exists(DATA_FILE):
        return
    #불러올 때뿐만 아니라 저장할 때도 항상 프로젝트 폴더의 subscriptions.json을 사용
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        loaded_data = json.load(file)

    subscriptions.update(loaded_data)