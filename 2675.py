n=int(input())
for _ in range(n):
    chrslist = []
    p = list(map(str,input().split()))
    num=int(p[0])
    char=p[1]
    chList=list(char)
    for cha in chList:
        for _ in range(num):
            chrslist.append(cha)
    print(''.join(chrslist))