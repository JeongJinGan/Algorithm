import sys

sys.stdin = open("2025_input.txt", "r")

T = int(input())
sum = 0
for i in range(1, T+1):
    sum += i
print(sum)    