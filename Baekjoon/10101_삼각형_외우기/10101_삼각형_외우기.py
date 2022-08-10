import sys

sys.stdin = open("10101.txt", "r")

list_ = []
for _ in range(3):
    angle = int(input())
    list_.append(angle)

if list_.count(60) == 3:
    print('Equilateral')
elif sum(list_) == 180 and len(set(list_)) == 2:
    print("Isosceles")
elif sum(list_) == 180 and len(set(list_)) == 3:
    print("Scalene")
else:
    print("Error")
