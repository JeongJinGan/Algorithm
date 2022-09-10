import sys
import statistics

sys.stdin = open("15719.txt", "r")

T = int(sys.stdin.readline().rstrip())
list_ = [0] * T
nums = list(map(int, sys.stdin.readline().split()))
for i in nums:
        list_[i] += 1
print(list_.index(max(list_)))
# print(statistics.mode(nums))
