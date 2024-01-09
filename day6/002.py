# 숫자 타입 -> 타입마다 사용할 수 있는 연산, 함수가 다르다
# 산술연사 : +, -, *, /, //, %
# 10과 3.14 변수
num1, num2 = 10, 3.14
# + - * /   ->  결과 출력 - 한줄로
print(f'합계 : {num1 + num2}\n뺄셈 : {num1 - num2}\n곱셈 : {num1 * num2}\n나눗셈 : {num1 / num2}')

num2= 3
print(f'목 : {num1//num2}\n나머지 : {num1%num2}')

# 함수 : 이름을 가진 기능 -> 재사용, 내장함수(import x)
# num1의 절대값 출력
print(abs(num1))