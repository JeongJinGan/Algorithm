a = int(input())
j = a-1 # 공백을 입력값(a)보다 1작은 상태로 초기화
for i in range(1, a+1):
    print(' ' * j, end ='') # 공백(j)을 먼저 출력
    j -= 1 # 공백이 점점 줄어야하기 때문에 -1씩 줄인다
    print('*' * i)
