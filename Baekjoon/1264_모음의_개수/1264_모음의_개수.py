import sys

sys.stdin = open("1264.txt", "r")

vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

while True:
    list_ = input()
    if list_ == '#':
        break

    cnt = 0
    for vowel in list_:
        if vowel in vowels:
            cnt += 1
  
    print(cnt)
    
