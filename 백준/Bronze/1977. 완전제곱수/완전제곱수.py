m = int(input())
n = int(input())

list_ = []

for i in range(m, n+1):
    root = int(i ** 0.5)
    if i == root ** 2:
        list_.append(i)

if list_ == []:
    print(-1)
else:
    print(sum(list_))
    print(min(list_))