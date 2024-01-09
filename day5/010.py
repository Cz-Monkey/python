list1 = [15, 20, 30, 90]
# #list1의 길이를 재라 -> len()x

# a = 0
# for x in list1:
#     a += 1
# print(a)

# list1의 합계를 출력하시오
# for x in list1:
#     y = sum(list1)
# print(y)

# hap = 0
# for x in list1:
#     hap = hap + x
# print(hap)

# list1의 평균(합계/개수)을 출력하시오
# len = 0
# for x in list1:
#     len += 1
#     avg = sum(list1) / len
# print(avg)

hap = 0
size = 0
for k in list1:
    hap += k
    size += 1
print(hap / size)
