import sys

sys.stdin = open("1945_input.txt", "r")

T = int(input())
for i in range(1, T+1):
    a = int(input())
    few = [2, 3, 5, 7, 11]
    cnt = [0] * 5
    for j in range(len(few)):
        while True:
            if a % few[j] == 0:
                a = a // few[j]
                cnt[j] += 1
            else:
                break
    print(f'#{i} ', end='')
    print(*cnt)

