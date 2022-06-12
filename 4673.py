def d(n):
    thousand = n//1000
    hundred = (n%1000)//100
    ten = (n%100)//10
    one = n%10
    num = n + thousand + hundred + ten + one
    return num

for i in range(10000):
    if 10000 > d(i):
        print(d(i))


