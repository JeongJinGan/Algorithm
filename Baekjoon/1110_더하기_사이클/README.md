```python
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
```



주석 / 비주석 코드의 차이를 잘 모르겠다.

1. 처음 입력받은 변수를 다시 다른 변수의 저장해서 사용하는 것.
2. 예를 들어 26입력 받는다면 다음으로 68로 될때의 변수.

이 두가지의 차이가 실행시간에도 차이가 있는지는 모르겠다.

