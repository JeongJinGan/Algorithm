import sys

sys.stdin = open("2446.txt", "r")

n = int(input())

j = 0
for i in range(2*n-1,0,-2):
    print(" "*j, end="")
    print("*"*i)
    j += 1

j = n-2
for i in range(3,2*n,2):
    print(" "*j, end="")
    print('*'*i)
    j -= 1


