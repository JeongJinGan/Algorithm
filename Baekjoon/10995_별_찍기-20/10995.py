a = int(input())
for i in range(1, a+1):
    if i%2 == 1: # 각 행이 홀수 일때
        for j in range(1, a+1):
            print('*', end='') # *먼저
            print(' ', end='') 
        print()
    else:   # 각 행이 짝수 일때
        for j in range(1, a+1):            
            print(' ', end='') # 공백 먼저
            print('*', end='')
        print()    