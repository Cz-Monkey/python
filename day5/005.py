# set - 중복불가능하고 순서가 없다
#     - 정렬된 것처럼 보여도 우연일 뿐
셋 = {1, 2, 3, 4}
print(셋)
셋.add(5)
print(셋)

# 리스트나 튜플은 중복이 가능하고 순서가 있다
리스트 = [1, 3, 4, 6, 1, 4, 2]
set2 = set(리스트)
리스트 = list(set2)
print(리스트)