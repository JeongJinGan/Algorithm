import sys

sys.stdin = open("1966_input.txt", "r")

T = int(input())

for i in range(1, T+1):
    a = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    print(f'#{i} ',end='')
    for j in range(a):
        print(nums[j], end =' ')
    print()  