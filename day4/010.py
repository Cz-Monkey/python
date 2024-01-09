# 숫자를 입력받아 양수, 음수, 0을 출력
# num = int(input("숫자 입력 : "))
# if num > 0:
#     result = "양수"
# elif num < 0:
#     result = "음수"
# else:
#     result = "0"
# print(f'{result} 입니다')

# 점수를 입력받아 70~90점이면 "추천대상", 아니면
# "대상아님" 이라고 출력
jumsu = int(input("점수 입력 : "))
if jumsu >= 70 and jumsu <= 90:
    result = "추천대상"
else:
    result = "대상아님"
print(f'추천 여부 : {result}\n수고하셨습니다')