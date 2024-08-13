def add_menu(item_list): 
        selected = []
        print(f'1. {item_list[0]}')
        print(f'2. {item_list[1]}')
        print(f'3. {item_list[2]}')
        print(f'4. {item_list[3]}')
        print(f'5. {item_list[4]}')
        print(f'6. {item_list[5]}')

        print('10. 동작취소')

        while True:
            user_input = input()

            print(f'선택 : {user_input}')
            if user_input == 1:
                selected = item_list[0]
                break
            elif user_input == 2:
                selected = item_list[1]
                break
            elif user_input == 3:
                selected = item_list[2]
                break
            elif user_input == 4:
                selected = item_list[3]
                break
            elif user_input == 5:
                selected = item_list[4]
                break
            elif user_input == 6:
                selected = item_list[5]
                break
            elif user_input == 10:
                print('취소')
                break
            else: 
                print('잘못 입력하셨습니다 다시 입력하세요')