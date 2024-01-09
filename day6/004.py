# f문자열
# replace : 치환
str4 = '010-1111-2222'
# 함수 : 소속없는 함수 + 소속있는 메소드(method)
print(len(str4))
# method : 특정 타입 소속    ->     타입은 함수도 가질 수 있다
# 문자열 메소드는 새로운 문자열을 만든다
str4 = str4.replace('-','.')

str4 = str4.replace('1111','xxxx')
print(str4)

# '971011-2******'
j1 = '971011-2010015'
j1 = j1.replace(j1[8:], '*'*6)
print(j1)

# 양 옆 공백을 지워주는 함수    ->  문자 사이 내용은 지우지 않는다
str5="  aa aa   "
print(str5.strip())