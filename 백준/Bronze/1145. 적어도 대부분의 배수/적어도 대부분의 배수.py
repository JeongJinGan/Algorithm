number = list(map(int, input().split()))
cnt = min(number)

while True:
    check = 0
    for i in number:
        if cnt % i == 0:
            check += 1
    if check > 2:
        break     
    cnt +=1
print(cnt)
