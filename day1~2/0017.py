# 숫자 2개를 입력받아 큰수와 작은수를 출력하시오
# 예 : 5와 8중 큰 수는 8, 작은수는 5입니다
num1 = int(input("첫번쨰 수 : "))
num2 = int(input("두번쨰 수 : "))
max = max(num1, num2)
min = min(num1, num2)
print(f'{num1}와(과) {num2} 중에 큰 수 : {max}\n{num1}와(과) {num2} 중에 작은 수 : {min}')