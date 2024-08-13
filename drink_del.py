def remove_menu(item_list):
    print(item_list.current_item)
    del_drinK = (input("어떤 음료를 삭제하시겠습니까?"))   
    
    if del_drinK in item_list.current_item : 
            item_list.current_item.remove(del_drinK)
            print("주문이 취소되었습니다.") 