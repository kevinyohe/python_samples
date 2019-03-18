from collections import deque


a = deque('THE GOOD OLD DAYS OF SCROLLERS!!!')

for x in range(1,30000):
    letter = a.pop()
    a.appendleft(letter)
    for elem in a:
        print(elem.upper())
    print('\n')