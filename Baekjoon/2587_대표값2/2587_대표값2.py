import sys

sys.stdin = open("2587.txt", "r")
list_ = []
for _ in range(5):
    nums = int(input())
    list_.append(nums)
    
sum_ = sum(list_)
avg_ = sum_//5
print(avg_)
list_.sort()
print(list_[2])