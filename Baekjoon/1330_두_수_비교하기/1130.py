num1, num2 = map(int, input().split())
if num1 > num2: # 입력받은 두 수 비교
    print('>') # 왼쪽 값이 더 크다면
elif num1 < num2: # 오른쪽 값이 더 크다면
    print('<')
else:   # 둘 다 아니라면
    print('==')