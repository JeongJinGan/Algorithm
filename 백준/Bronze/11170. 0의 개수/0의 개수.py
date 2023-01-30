T = int(input())

for i in range(T):
    N, M = map(int,input().split())
    list_ = []
    for j in range(N, M+1):
        list_.append(j)
    list_ = str(list_)
    print(list_.count('0'))