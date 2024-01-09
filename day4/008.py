# 1년은 몇초인지 출력
DAYS_PER_YEARS = 365
HOURS_PER_DAYS = 24
MINUTES_PER_HOURS = 60
SECONDS_PER_MINUETS = 60
print(DAYS_PER_YEARS * HOURS_PER_DAYS * MINUTES_PER_HOURS * SECONDS_PER_MINUETS)

# 45분간 일하고 10분씩 휴식, 전체 근무시간 480분이면
# 휴식 시간의 합계는 얼마인가?
일 = 45
휴식 = 10
총근무시간 = 480
세트 = 일 + 휴식 
휴식시간합계 = 총근무시간 // 세트
print(휴식시간합계)