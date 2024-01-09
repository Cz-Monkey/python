members = []
while True:
    print("=======메뉴 선택=======")
    print("1. 숫자 추가")
    print("2. 숫자 출력")
    print("3. 합계")
    print("4. 값으로 삭제")
    print("999. 숫자 추가")
    input_num = input('숫자 입력 : ')
    if input_num == '1':
        num = int(input('추가 할 숫자 : '))
        members.append(num)
    elif input_num == '2':
        print (f'숫자 출력 : {members}')
    elif input_num == '3':
        print (f'합계 : {sum(members)}')
    elif input_num == '4':
        num2 = int(input('삭제 할 값 : '))
        if num2 in members:
            members.remove(num2)
            print(f'삭제 후 값 : {members}')
        else:
            print('삭제 할 값이 없습니다')
    elif input_num == '999':
        print('종료합니다')
        break