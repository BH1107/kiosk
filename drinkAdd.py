def add_menu(item_list): 
        print(f'1. {item_list.item[0]}')
        print(f'2. {item_list.item[1]}')
        print(f'3. {item_list.item[2]}')
        print(f'4. {item_list.item[3]}')
        print(f'5. {item_list.item[4]}')
        print(f'6. {item_list.item[5]}')

        print('10. 동작취소')

        while True:
            user_input = input()

            print(f'선택 : {user_input}')
            if user_input == 1:
                item_list.current_item.append(item_list.item[0])
                break
            elif user_input == 2:
                item_list.current_item.append(item_list.item[1])
                break
            elif user_input == 3:
                item_list.current_item.append(item_list.item[2])
                break
            elif user_input == 4:
                item_list.current_item.append(item_list.item[3])
                break
            elif user_input == 5:
                item_list.current_item.append(item_list.item[4])
                break
            elif user_input == 6:
                item_list.current_item.append(item_list.item[5])
                break
            elif user_input == 10:
                print('취소')
                break
            else: 
                print('잘못 입력하셨습니다 다시 입력하세요')