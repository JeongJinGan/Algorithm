T = int(input())

N = list(map(int, input().split()))
N.sort()
su = N[0] * N[-1] 
print(su)