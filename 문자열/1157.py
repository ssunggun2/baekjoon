import collections
from itertools import count
s=input()
s=list(s.lower())
counter = collections.Counter(s)
if len(counter) > 1:
    most = counter.most_common()[0]
    sec = counter.most_common()[1]
    if most[1] == sec[1]:
        print('?')
    else:
        print(most[0].upper())
else:
    print(counter.most_common()[0][0].upper())