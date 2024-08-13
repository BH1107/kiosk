def add_menu(item_list): 
        item_key = item_list.item.keys()
        item_key_list = list(item_key)
        print('1. 아메리카노')
        print(f'2. 카페라떼')
        print(f'3. 콜드브루')
        print(f'4. 에스프레소')
        print(f'5. 아이스티')
        print(f'6. 말차라떼')

        print('10. 동작취소')

        while True:
            user_input = input()

            print(f'선택 : {user_input}')
            if user_input == '1':
                item_list.current_item.append(item_key_list[0])
                break
            elif user_input == '2':
                item_list.current_item.append(item_key_list[1])
                break
            elif user_input == '3':
                item_list.current_item.append(item_key_list[2])
                break
            elif user_input == '4':
                item_list.current_item.append(item_key_list[3])
                break
            elif user_input == '5':
                item_list.current_item.append(item_key_list[4])
                break
            elif user_input == '6':
                item_list.current_item.append(item_key_list[5])
                break
            elif user_input == '10':
                print('취소')
                break
            else: 
                print('잘못 입력하셨습니다 다시 입력하세요')