n = int(input())

def getPoint(x):
    point = 0
    sum = 0
    for j in x:
        point += 1
        if j == 'X':
            point = 0
        sum = sum + point
        
    return sum

for _ in range(n):
    ox_list = str(input())
    point=getPoint(ox_list)
    print(point)