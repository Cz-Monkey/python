# 숫자를 제곱하는 함수 : 
def jegop(num:int)->int:
    # int가 아니면 실패 -> int 어떻게? 실패는 뭐지?
    if isinstance(num, int)==False:
        return 0
    return (num*num)

