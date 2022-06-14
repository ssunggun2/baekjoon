s=input()
sList=list(s)
times = []
for i in sList:
    if i in ['A','B','C']:
        times.append(3)
    if i in ['D','E','F']:
        times.append(4)
    if i in ['G','H','I']:
        times.append(5)
    if i in ['J','K','L']:
        times.append(6)
    if i in ['M','N','O']:
        times.append(7)
    if i in ['P','Q','R','S']:
        times.append(8)
    if i in ['T','U','V']:
        times.append(9)
    if i in ['W','X','Y','Z']:
        times.append(10)

print(sum(times))