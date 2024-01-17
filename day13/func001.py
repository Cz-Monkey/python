def sample1():
    return 10

# 나이를 입력받아 성년/미성년을 판단
def is_major(nai:int)->bool:
    return nai >= 18

# 나이를 입력받아 입장료를 리턴하는 함수
# 25~64세면 3000원, 기타는 무료

def is_nai(num:int)->int:
    if num > 24 and num <= 64:
        return 3000
    else:
        return 0
    
# 입장료는 3000원이다. 10명이면 1인당 2400원이다
# 인원수를 입력받아 요금을 출력

def is_pay(member:int)->int:
    if member > 9:
        return member * 2400
    else:
        return member * 3000