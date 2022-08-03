import sys

sys.stdin = open("15953.txt", "r")

prize1 = {
    500 : 1,
    300 : 2,
    200 : 3,
    50 : 4,
    30 : 5,
    10 : 6
}
prize2 = {
    512 : 1,
    256 : 2,
    128 : 4,
    64 : 8,
    32 : 16
}

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    a_result = 0
    b_result = 0
    rank = 0

    if a > 0:
        for key, value in prize1.items():
            rank += value
            if a <= rank:
                a_result += key
                break
    rank = 0

    if b > 0:
        for key, value in prize2.items():
            rank += value
            if b <= rank:
                b_result += key
                break
    
    print((a_result + b_result) * 10000)




