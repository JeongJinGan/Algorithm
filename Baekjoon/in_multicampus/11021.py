test_case = int(input())
for i in range(1,test_case+1):
    num1 , num2 = map(int, input().split())
    print(f'Case #{i}: {num1 + num2}')