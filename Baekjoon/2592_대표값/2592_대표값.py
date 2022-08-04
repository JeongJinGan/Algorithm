import sys

sys.stdin = open("2592.txt", "r")

sum_ = 0
list_ =[]
for _ in range(10):
    num = int(input())
    list_.append(num)
    sum_ += num

print(sum_//10)
print(max(list_, key = list_.count))

