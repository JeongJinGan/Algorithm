import sys

sys.stdin = open("10815.txt", "r")

M = int(sys.stdin.readline())
# set()을 안하면 시간초과가 뜬다.
# nums = list(map(int, sys.stdin.readline().split()))
nums = set(map(int, sys.stdin.readline().split()))
N = int(sys.stdin.readline())
nums2 = list(map(int, sys.stdin.readline().split()))


for i in nums2:
    if i in nums:
        print(1, end=" ")
    else:
        print(0, end=" ")

# 리스트를 새로 선언해서 비교한다음 1,0을 알맞게 넣는 방법으로 풀어가려했다
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