A = list(map(int, input().split()))
B = list(map(int, input().split()))
list_ = []

for i in range(0,10):
    if A[i] > B[i]:
        list_.append('A')
    elif A[i] < B[i]:
        list_.append('B')
    else:
        list_.append('D')

res1 = (list_.count('A'))
res2 = (list_.count('B'))


if res1 == res2:
    print('D')
elif max(res1, res2) == res1:
    print('A')
else:
    print('B')


