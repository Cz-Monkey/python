# control : 순서를 바꾼다
# 조건 : 결과가 이럴수도 저럴수도 있다
# jumsu가 짝수인지 홀수인지 출력해라(2의 배수)

jumsu = 75
if jumsu % 2 == 0:
    print(f'{jumsu}는 짝수입니다')
else:
    print(f'{jumsu}는 홀수입니다')
print('수고하셨습니다')

# 점수가 90점 이상이면 우수, 70점 이상 합격, 미만이면 재시험
jumsu = 90
if jumsu >= 90:
    print('우수')
elif jumsu >= 70:
    print("합격")
else:
    print('재시험')
print('수고하셨습니다')