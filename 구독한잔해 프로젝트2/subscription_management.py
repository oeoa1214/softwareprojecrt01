


from subscriptions import register_subscription, view_subscriptions,  delete_subscription
def subscription_management():
  while True:
   print("===== 구독 관리 =====")
   print("1. 구독 등록")
   print("2. 구독 조회")
   print("3. 구독 삭제")
   print("0. 뒤로가기")
 #설계서 선택:이라고 되어있는데 존댓말로 수정
 # 앞뒤 공백 제거
   menu = input("메뉴를 선택해주세요: ").strip()
   #설계서에서는 1.5, 2.0처럼 정수가 아닌 숫자 입력은  잘못된 메뉴 입력입니다. 0~3 중 하나의 번호만 입력해주세요.
   #라고 되어 있는데 그럴려면 너무 복잡해져서 그래서 하나의 번호를 입력해주세요로 수정하는걸로!
   # Enter만 누른 경우
   if menu == "":
      print("메뉴 번호를 입력해주세요. 0~3 중 하나의 번호를 입력해주세요.")
      continue

   if menu == "1":
      register_subscription()

   elif menu == "2":
      view_subscriptions()

   elif menu == "3":
      delete_subscription()

   elif menu == "0":
      return

   else:
      print("잘못된 메뉴 입력입니다. 0~3 중 하나의 번호를 입력해주세요.")