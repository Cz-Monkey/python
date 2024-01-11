todos = []
# 할일 : 할일번호, 할일, 완료
todos.append({'tno':1, 'title':'자바 공부', 'finish':False})
todos.append({'tno':2, 'title':'스프링 공부', 'finish':False})
todos.append({'tno':3, 'title':'파이썬 공부', 'finish':False})
tno = 4

def print_todos():
    for todo in todos:
        print(todo)

def add_todo():
    # 함수 안에서 함수 밖에 있는 변수를 사용하려면 global 변수이름
    global tno4
    title = input('할일 입력 : ')ㅍ ㅠ퓿
    todos.append({'tno':tno, 'title':title, 'finish':False})
    tno = tno+1

# 숫자를 입력받아 리스트에서 tno을 찾아 finish를 True로 바꿔라....
def toggle_finish():
    input_todo = int(input('숫자 입력 :'))
    for todo in todos:
        if input_todo == todo['tno']:
            todo['finish'] = not todo['finish']

def delete_todo():
    for todo in todos:
        if todo['finish'] == True:
            todos.remove(todo)

try:
    while True:
        print('### 할일 관리 ###')
        print('1:목록, 2:할일 추가, 3:변경, 4:삭제, 999:종료')
        select = input('메뉴 선택 : ')
        if  select == '1':
            print_todos()                # 호출한다
        elif select == '2':
            add_todo()
        elif select == '3':
            toggle_finish()
        elif select == '4':
            delete_todo()
        elif select == '999':
            print('이용해주셔서 감사합니다')
            break
except:
    print('숫자를 입력하세요')