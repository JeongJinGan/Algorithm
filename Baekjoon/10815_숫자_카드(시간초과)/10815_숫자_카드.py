import sys

sys.stdin = open("10815.txt", "r")

M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

N = int(sys.stdin.readline())
nums2 = list(map(int, sys.stdin.readline().split()))


for i in nums2:
    if i in nums:
        print(1, end=" ")
    else:
        print(0, end=" ")
# list_ = [0] * N
# k = 0       
# for i in nums2:
#     if i in nums:
#         list_[k] = 1
#         k += 1
#     else:
#         list_[k] = 0
#         k += 1 

# print(*list_)