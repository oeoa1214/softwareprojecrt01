from subscriptions import subscriptions

def to_monthly(cost, cycle):
    if cycle == "월간":
        return cost
    elif cycle == "4주":
        return cost * 13 / 12
    elif cycle == "연간":
        return cost / 12

def normalize_subscriptions():
    if not subscriptions:
        print("등록된 구독이 없습니다.")
        return

    total_monthly_cost = 0
    print("===== 결제 주기 정규화 =====")
    print("[서비스별 월 환산 비용]")

    for key, value in subscriptions.items():
        monthly_cost = to_monthly(float(value["cost"]), value["cycle"])
        print(f"{key}: {monthly_cost:,.2f}원")
        total_monthly_cost += monthly_cost

    print("")
    print(f"전체 월 지출: {total_monthly_cost:,.2f}원")
    print("")
    print("[카테고리별 월 지출]")

    category_totals = {}

    for key, value in subscriptions.items():
        monthly_cost = to_monthly(
            float(value["cost"]),
            value["cycle"]
        )

        category = value["category"]

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += monthly_cost

    for category, total in category_totals.items():
        print(f"{category}: {total:,.2f}원")