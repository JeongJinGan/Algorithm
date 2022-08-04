import sys

sys.stdin = open("9093.txt", "r")

T = int(input())
for _ in range(T):
    list_ = list(input().split())
    
    for over in list_:
        print(over[::-1], end = " ")
    print()

