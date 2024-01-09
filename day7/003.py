# 할일 관리
todos = [
    {'tno':1, 'title':'할일1', 'reg_dat':'2024-01-09', 'finish':False},
    {'tno':3, 'title':'할일3', 'reg_dat':'2024-01-09', 'finish':False}
]
tno = 2
# Read : 전체읽기, 1개읽기
for todo in todos:
    print(todos)

# 할일 번호를 일력받아 찾아서 출력
input_num = int(input('숫자 입력 : '))
찾았니 = False
for todo in todos:
    if todo['tno'] == input_num:
        print(todo)
        찾았니 = True
        break
if 찾았니 == False:
    print('할일을 찾을 수 없습니다')