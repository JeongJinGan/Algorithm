# https://www.acmicpc.net/problem/2711
import sys

sys.stdin = open("2711_오타맨_고창영.txt", "r")

Test_case = int(input())
a_word = []
for i in range(Test_case):
    index_, word = input().split()
    index_ = int(index_)
    word_ = list(word)  
    word_.pop(index_-1)
    a_word.append(word_) 

for j in a_word:
    for k in j:
        print(k, end= '')
    print()    


# 4
# 4 MISSPELL => MISPELL
# 1 PROGRAMMING
# 7 CONTEST
# 3 BALLOON