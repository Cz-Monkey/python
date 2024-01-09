# 연산
# 산술연산
# +, -, *, /
# 몫 : //, 나머지 : %
print(18/5)
print(18//5)
print(17%5)

x = 15.82
# x의 소수점 이하를 버리고 출력
print(int(x))
print(x//1)

a = 19
b = 5
a,b = 19,5
# %연산 금지, 나머지를 출력하시오
print(a-(b*(a//b)))
nmg = a-((a//b)*b)
print(nmg)

y = 453
# y를 1의 자리에서 버림 : 450(산술연산)
result = y-(y%10)
print(result)

# %금지
result = (y//10)*10
print(result)
print(y//100*100)

# 숫자를 입력하면 그 숫자보다 작은 최대의 짝수
# 7 -> 6

# # case1
# input_num = --2int(input("숫자를 입력하시오 : "))
# if input_num > 0:
#     if input_num >= input_num % 2 == 0:
#         result = input_num
#     elif input_num % 2 != 0:
#         result = input_num - 1
# elif input_num < 0:
#     if input_num <= input_num % 2 == 0:
#         result = (input_num)
#     elif input_num % 2 != 0:
#         result = (1 + input_num)
# else:
#     print("0을 제외한 정수를 넣어주세요")
# print(f'{input_num}의 최대의 짝수 : {result}')

# # case2
# input_num = int(input("숫자를 입력하시오 : "))
# if input_num >= input_num % 2 == 0:
#     if input_num > 0:
#         result = input_num
#     elif input_num < 0:
#         result + input_num
# elif input_num < input_num % 2 != 0:
#     if input_num > 0:
#         result = input_num - 1
#     elif input_num < 0:
#         result = 1 + input_num
# else:
#     print("0을 제외한 정수를 넣어주세요")
# print(f'{input_num}의 최대의 짝수 : {result}')
    

# 숫자를 입력하면 가장 가까운 7의 배수 출력
# 15 -> 21
# input_num = int(input("숫자를 입력하시오 : "))
input_num = 14
large_num = (input_num//7)*7
near_num = (input_num%7)
if large_num :
    result = large_num
else:
    result = near_num
print(f'가장 가까운 7의 배수는 : {result}')