import sys

sys.stdin = open("11943.txt", "r")

a1, o1 = map(int, input().split())
a2, o2 = map(int, input().split())
print(min(a1+o2,o1+a2))