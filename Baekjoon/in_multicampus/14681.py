# x, y = map(int, input().split()) map함수를 쓰니 런타임 에러가 났다.
x = int(input())
y = int(input())
if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
else:
    print('4')