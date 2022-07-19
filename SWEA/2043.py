import sys

sys.stdin = open("2043_input.txt", "r")

a, b = map(int, input().split())
print(a-b+1)
    