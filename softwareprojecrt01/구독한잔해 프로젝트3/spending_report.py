from subscriptions import subscriptions
from payment_normalizer import to_monthly

def spending_report():
    if not subscriptions:
        print("등록된 구독이 없습니다.")
        return

    print("===== 체감 지출 리포트 =====")
    total_monthly_cost = 0
    #총 월 환산 비용 계산을 구한 다음에 그걸 12를 곱해서 연간 예상 지출액을 구한다.
    # 그 다음 연간 예상 지출액을 출력하고 그걸 커피 가격으로 나누어서 연간 예상 지출액을 커피로 환산한 값을 출력한다
    for key, value in subscriptions.items():
        monthly_cost = to_monthly(float(value["cost"]), value["cycle"])
        total_monthly_cost += monthly_cost
        
    print(f"연간 예상 지출액: {12 * total_monthly_cost:,.2f}원")
    print(f"커피 5000원 기준: {12 * total_monthly_cost / 5000:.2f}잔")
       

 
