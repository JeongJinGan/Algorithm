x = int(input())

n = 64
cnt = 0

arr64 = [64,32,16,8,4,2,1]

for i in arr64:
    if(x-i>=0):
        x = x - i
        cnt += 1
        if(x == 0):
            print(cnt)   
