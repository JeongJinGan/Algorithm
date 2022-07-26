import sys

sys.stdin = open("1948_input.txt", "r")

T = int(input())
for i in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())
    month_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = 0
    for j in range(m1, m2):
        if m1 == j:
            result += month_day[j] - d1 +1
        else:
            result += month_day[j]
    result += d2
    print(f'#{i} {result}')
