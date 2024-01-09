# 숫자 리스트 - 추가, 목록, 변경, 삭제. 함수버전
numbers=[]

def print_menu():
    print('############## 숫자 CRUD ##############')
    print('1:추가, 2:목록, 3:삭제, 999:종료')

def input_select():
    return input('메뉴 선택 : ')

def add_value():
    value = int(input('값 입력 : '))
    numbers.append(value)

def list_numbers():
    print(numbers)

def delete_number():
    value2 = int(input('삭제 할 값 : '))
    if value2 in numbers:
        numbers.remove(value2)
    else:
        print('삭제할 값이 없습니다')


def finish():
    print('종료합니다')

while True:
    print_menu()
    select = input_select()
    if select == '1':
        add_value()
    elif select == '2':
        list_numbers()
    elif select == '3':
        delete_number() 
    elif select == '999':
        finish()
        break