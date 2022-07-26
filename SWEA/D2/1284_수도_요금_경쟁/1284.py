# import sys

# sys.stdin = open("1284_input.txt", "r")

# T = int(input())
# mim = 0
# for i in range(1, T+1):
#     p,q,r,s,w = map(int, input().split())
#     a = p*w

#     if w < r:
#         b = q
#     else:
#         b = q + (w-r)*s
      
#     if a < b:
#         min = a

#     else:
#         min = b

#     print(f'#{i} {min}')

import sys

sys.stdin = open("1284_input.txt", "r")

T = int(input())
mim = 0
for i in range(1, T+1):
    p,q,r,s,w = map(int, input().split())
    a = p*w

    if w < r:
        b = q
    else:
        b = q + (w-r)*s

    print(f'#{i} {min(a,b)}')