N = list(map(int, input().split()))

for i in range(len(N)):
    for j in range(1, len(N)):
        if N[j] < N[j-1]:
            N[j], N[j-1] = N[j-1], N[j]
            print(' '.join(map(str,(N)))) 