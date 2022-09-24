import sys

sys.stdin = open("1475.txt", "r")

room_num = input()
list_ = [0] * 9

for i in room_num:
    num = int(i)
    if num == 9:
        num = 6
    
    list_[num] += 1

list_[6] = (list_[6]+1) // 2
print(max(list_))


