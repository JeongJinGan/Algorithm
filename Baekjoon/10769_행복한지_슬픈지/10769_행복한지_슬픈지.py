import sys

sys.stdin = open("10769.txt", "r")


my_feel = input()

happy = my_feel.count(':-)')
sad = my_feel.count(':-(')

if happy == 0 and sad == 0:
    print('none')
elif happy > sad:
    print('happy')
elif happy < sad:
    print('sad')
else:
    print('unsure')




