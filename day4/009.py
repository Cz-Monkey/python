# 숫자를 입력받아 1의 자리까지 버리고 출력
# 예) 3512 -> 3510, 359 -> 350
# num = int(input("숫자 입력 : "))
# result = (num // 10) * 10
# print(f'값 : {result}')

# num = int(input("숫자 입력 : "))
# result = num - num % 10
# print(f'값 : {result}')

# 자연수를 입력받아 그 숫자보다 작거나 같은 최대의 7의 배수
# 17 -> 14, 21 -> 21

# num = int(input("숫자 입력 : "))
# large_num = (num // 7) * 7
# if num >= large_num:
#     result = large_num
# else:
#     print("다시 입력하시오")
# print(f'값 : {result}')

# 자연수를 입력받아 그 숫자보다 작은 최대의 7의 배수
# 예) 17 -> 14, 21 -> 14
num = int(input("숫자 입력 : "))
large_num = (num // 7) * 7
if num == large_num:
    result = num - 7
elif num > large_num:
    result = large_num
else:
    print("다시 입력하시오")
print(f'값 : {result}')

