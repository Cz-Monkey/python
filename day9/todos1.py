todos = []
# 할일 : 할일번호, 할일, 완료
todos.append({'tno':1, 'title':'자바 공부', 'finish':False})
todos.append({'tno':2, 'title':'스프링 공부', 'finish':False})
todos.append({'tno':3, 'title':'파이썬 공부', 'finish':False})

while True:
    print('### 할일 관리 ###')
    print('1:목록, 2:할일 추가, 3:변경, 4:삭제, 999:종료')
    select = input('메뉴 선택 : ')
    if  select == '1':
        print('목록')
    elif select == '2':
        print('추가')
    elif select == '3':
        print('변경')
    elif select == '4':
        print('삭제')
    elif select == '999':
        print('이용해주셔서 감사합니다')
        break