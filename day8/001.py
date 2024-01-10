# 나이를 입력받아 성녀, 미성년을 리턴하는 함수


def is_adult(nai:int):
    if nai >= 18:
        return True
    else:
        return False

nai = 25
if is_adult()=="성년":
    print('당신은 출입가능합니다')