# https://www.acmicpc.net/problem/5622
import sys

sys.stdin = open("5622_다이얼.txt", "r")

daieol = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
call = input()
sum = 0
for i in range(len(call)):
    for j in daieol:
        if call[i] in j:
            sum += daieol.index(j)+3

print(sum)

# 코드리뷰

# dict_ = {
#     "A" : 2, "B" : 2, "C" : 2,
#     "D" : 3, "E" : 3, "F" : 3,
#     "G" : 4, "H" : 4, "I" : 4,
#     "J" : 5, "K" : 5, "L" : 5,
#     "M" : 6, "N" : 6, "O" : 6,
#     "P" : 7, "Q" : 7, "R" : 7, "S" : 7,
#     "T" : 8, "U" : 8, "V" : 8,
#     "W" : 9, "X" : 9, "Y" : 9, "Z" : 9
# }

# time_ = 0
# string = 'UUNICC'

# for key in string:
#     # if문으로 한다면 이렇게 전부해줘야함
#     # if key == 'A':
#     #     number = 1
#     # if key in ["A","B","C"]:
#     #     number = 1
#     # 딕셔너리 변수에 key로 접근
#     number = dict_[key]
#     print(key, number)
#     time_ += number + 1
# print(time_)