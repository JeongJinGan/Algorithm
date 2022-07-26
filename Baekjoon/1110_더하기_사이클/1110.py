N = int(input()) #26
cnt = 0
num = N
while True:  
    cut = N // 10   # 몫 2
    rest = N % 10   # 나머지 6
    r_plus_c = (rest + cut) % 10    # 6 + 2 = 8 => 십의 자리일 경우 일의자리만 
    N = (rest * 10) + r_plus_c    # 60 + 8 = 68
    cnt += 1

    if (N == num):
        break
print(cnt)

# 시간초과
# N = int(input()) #26
# cnt = 0
# while True:  
#     cut = N // 10   # 몫 2
#     rest = N % 10   # 나머지 6
#     r_plus_c = (rest + cut) % 10    # 6 + 2 = 8 => 십의 자리일 경우 일의자리만 
#     new_num = (rest * 10) + r_plus_c    # 60 + 8 = 68
#     cnt += 1
    
#     if new_num == num:
#         break
# print(cnt)