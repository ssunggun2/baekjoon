def d(n):
    thousand = n//1000
    hundred = (n%1000)//100
    ten = (n%100)//10
    one = n%10
    num = n + thousand + hundred + ten + one
    return num

iList = []
dList = []
for i in range(10000):
    iList.append(i)
    if 10000 > d(i):
        dList.append(d(i))

a_sub_b = [x for x in iList if x not in dList]
for k in a_sub_b:
    print(k)
