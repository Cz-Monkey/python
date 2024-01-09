# 몇일인지 입력받아 몇개월 며칠인지 출력
# 333 -> 11개월 3일
# 코드에 값이 직접 나타나는 것 : literal
DAY_PER_MONTH = 30
days = 333 
months = days//DAY_PER_MONTH
days = days%DAY_PER_MONTH
print(f"{months}개월 {days}일")
