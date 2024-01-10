# 두 숫자를 입력받아 큰 수를 가리는 함수
def large(a:int, b:int):
    if a > b:
        return True
    else:
        return False
    
# 숫자를 입력받아 절대값을 계산하는 함수
def abs_number(a:int):
    if a<0:
        return -a
    return a