# 숫자를 입력받아 3의 배수인지 아닌지 출력하시오
num = int(input("숫자 입력 : "))
if num % 3 == 0:
    print(f'{num}는 3의 배수입니다')
else:
    print(f'{num}는 3의 배수가 아닙니다')

# 점수를 입력받아 90점이상이면 우수, 70점이상이면 패스, 미만이면 낙제라고 출력하시오
jumsu = int(input("점수 입력 : "))
if jumsu >= 90:
    print('우수입니다')
elif jumsu >=70:
    print('패스입니다')
else:
    print('낙제입니다')
print("수고하셨습니다")

