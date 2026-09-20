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
        print(f"{key}: {monthly_cost}원")
        total_monthly_cost += monthly_cost

    print("")
    print(f"전체 월 지출: {total_monthly_cost}원")
    print("")
    print("[카테고리별 월 지출]")

    OTT_total = 0
    video_total = 0
    productivity_total = 0
    music_total = 0
    etc_total = 0

    for key, value in subscriptions.items():

        monthly_cost = to_monthly(
            float(value["cost"]),
            value["cycle"]
        )

        if value["category"] == "OTT":
            OTT_total += monthly_cost

        elif value["category"] == "영상":
            video_total += monthly_cost

        elif value["category"] == "생산성":
            productivity_total += monthly_cost

        elif value["category"] == "음악":
            music_total += monthly_cost

        elif value["category"] == "기타":
            etc_total += monthly_cost

    print(f"OTT: {OTT_total}원")
    print(f"영상: {video_total}원")
    print(f"생산성: {productivity_total}원")
    print(f"음악: {music_total}원")
    print(f"기타: {etc_total}원")