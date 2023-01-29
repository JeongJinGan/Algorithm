N, K = map(int, input().split())
su = list(map(int, input().split(',')))

for i in range(K):
    B = []
    for j in range(len(su)-1):
        B.append(su[j+1] - su[j])
    su = B

print(*su, sep=',')