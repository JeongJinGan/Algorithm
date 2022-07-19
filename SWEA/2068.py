import sys

sys.stdin = open("2068_input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    a = list(map(int, input().split()))
    a_max = max(a)
    print(f'#{test_case} {a_max}')