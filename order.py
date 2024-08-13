def order(item_list):
    total_pay = 0
    for i in item_list.current_item:
        total_pay =+ item_list.item[i]
        
    print(f"주문 품목 총액은 {total_pay} 품목은 다음과 같습니다.")
    print(item_list.current_item)
    order_menu = int(input("주문하시겠습니까?"))
    if order_menu == 1 :
        print("주문이 완료되었습니다.")
        print("이용해주셔서 감사합니다.")
        return True
    elif order_menu == 2 :
        return False