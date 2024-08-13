

def check_menu(item_list):
    price = 0
    print('선택 : 3 Enter')
    for i in item_list.current_item:
        price += item_list.item[i]
    print(f'주문 품목 총액{price}입니다.')
    print(f'{item_list.current_item}')