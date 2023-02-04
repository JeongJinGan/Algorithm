n = int(input())

fi = [0, 1]

for i in range(2, n+1):

    f = fi[i-1] + fi[i-2] 
    fi.append(f)
    
print(fi[-1])