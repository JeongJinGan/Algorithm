import sys

sys.stdin = open("1936_input.txt", "r")

a,b = map(int, input().split())
if b-a == 1 or b-a == 2:
    print("B")
else:
    print("A")