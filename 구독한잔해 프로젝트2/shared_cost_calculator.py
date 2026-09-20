from payment_normalizer import to_monthly
from subscriptions import subscriptions
def caculator():
    print("===== 분담비용 계산기 =====")

    print("[등록된 구독 서비스]")
    for key in subscriptions:
            print(f"- {key}")

    service_name = input("계산할 서비스명을 입력해주세요: ")
    monthly_cost = to_monthly(float(subscriptions[service_name]["cost"]),subscriptions[service_name]["cycle"])
    #true_cost는 1인당 월 실부담액
    #1인당 실 부담액은 월 환산 비용/공유 인원수로 구한다.
    true_cost=monthly_cost/int(subscriptions[service_name]["shared_count"])
    print("===== 분담비용 계산 결과 ====")
    print(f"서비스명: { service_name}") 
    print(f"월 환산 비용: {monthly_cost}원")
    print(f"공유 인원수: {subscriptions[service_name]['shared_count']}명")
    print(f"1인당 월 실부담액: {true_cost}원")