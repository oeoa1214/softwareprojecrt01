from subscription_management import subscription_management
from subscriptions import save_subscriptions, load_subscriptions
from payment_normalizer import normalize_subscriptions
from spending_report import spending_report
from shared_cost_calculator import caculator
load_subscriptions()

while True:


    
    print("===== 구독한잔해 =====")
    print("1. 구독 관리")
    print("2. 결제 주기 정규화")
    print("3. 체감 지출 리포트")
    print("4. 분담비용 계산기")
    print("0. 저장 후 종료")

    #strip매서드 앞뒤 공백을 지움
    main_menu = input("메뉴를 선택해주세요: ").strip()

    # 그냥 엔터는 ""라서 다시 입력 하게 만듬
    if main_menu == "":
     print("메뉴 번호를 입력해주세요. 0~4 중 하나의 번호를 입력해주세요.")
     continue

    # else로 0 1 2 3 4 이외 입력 다시 입력하게 만듬  
    if main_menu == "1":
        subscription_management()

    elif main_menu == "2":
        normalize_subscriptions()

    elif main_menu == "3":
        spending_report()

    elif main_menu == "4":
        caculator()

    elif main_menu == "0":
        save_subscriptions()
        break

    else:
     print("잘못된 메뉴 입력입니다. 0~4 중 하나의 번호를 입력해주세요.")  

  