# 초를 입력받아 몇분 몇초인지 출력
# 예) 210초라고 입력하면 3분 30초
input_sec = 210
# 3 = 210 
min = input_sec//60
# 30 = 210 % 60
sec = input_sec%60
print(f'{min}분 {sec}초')

# 분과 초를 입력하면 초를 출력
# 5분 10초 -> 310초
# 코드에 값이 직접 나타나는 것 : literal
min = 5
sec = 10
# 상수는 대문자로
SECONDS_PER_MINUTE = 60
result = min * SECONDS_PER_MINUTE +sec
print(result)