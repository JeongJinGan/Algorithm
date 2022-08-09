import sys

sys.stdin = open("5800.txt", "r")

K = int(input())
for _ in range(K):
    score = list(map(int, input().split()))
    score.pop(0)
    score.sort(reverse= True)

    max_ = score[0]
    min_ = score[-1]
    largest_gap = 0
    print(f'Class {_+1}')   
    for i in range(len(score)-1):  
        gap = score[i+1] - score[i]
        if gap < largest_gap:
            largest_gap = gap
        
    print(f'Max {max_}, Min {min_}, Largest gap {-largest_gap}')




