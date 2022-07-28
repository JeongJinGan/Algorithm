N = int(input())
bestseller_ = dict()
for i in range(N):
    book = input()
    if book not in bestseller_:
        bestseller_[book] = 1
    else:
        bestseller_[book] += 1 

list_ = [] # 딕셔너리는 순서가 없기 때문에 리스트 생성

max_ = max(bestseller_.values())

# print(bestseller_.values())
print(bestseller_)
for j in bestseller_:
    if max_ == bestseller_[j]:
        list_.append(j)

list_.sort()
print(list_[0])

# print(max_)

# ex)
# 9
# table
# chair
# table
# table
# lamp
# door
# lamp
# table
# chair

# 8
# icecream
# peanuts
# peanuts
# chocolate
# candy
# chocolate
# icecream
# apple