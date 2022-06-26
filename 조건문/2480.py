import enum
a,b,c=map(int,input().split(' '))
prize = max(a,b,c)*100
numList = [a,b,c]
prize = max(numList)*100
for idx,i in enumerate(numList):
    count = numList.count(i)
    if count == 3:
        prize = 10000+1000*a
    if count == 2:
        prize = 1000+100*i
print(prize)


# Short 
*_,a,b,c=sorted(input());print(['1'+b,c][a<b<c]+'000'[a<c:])