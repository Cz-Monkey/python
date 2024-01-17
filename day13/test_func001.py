from func001 import is_major, is_nai, is_pay
# 테스트하는 함수를 작성
# 테스트하는 함수는 pytest로 실행이 가능
# def test_sample1():
#     assert sample1()==10

# def test_round():
#     assert round(2.5)==2

# def test_is_major():
#     assert is_major(20) is True
#     assert is_major(18) is True
#     assert is_major(15) is False

# def test_is_nai():
#     assert is_nai(25)==3000
#     assert is_nai(64)==3000
#     assert is_nai(24)==0
#     assert is_nai(65)==0

def test_is_pay():
    assert is_pay(10)==24000
    assert is_pay(11)==26400
    assert is_pay(9)==27000
    assert is_pay(8)==24000