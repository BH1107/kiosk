# 2. 음료 삭제 기능 구현


def REMOVE():
    print(current_item)
    del_drinK = (input("어떤 음료를 삭제하시겠습니까?"))   
    
    if del_drink in current_item : 
            current_item = current_item.remove(del_drinK)
            print("주문이 취소되었습니다.")  

    return current_item
