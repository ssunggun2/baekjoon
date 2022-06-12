n = int(input())
for _ in range(n):
    pointList = list(map(int,input().split()))
    n = pointList[0]
    meanPoint = sum(pointList[1:])/n
    count = 0
    for i in pointList[1:]:
        if i> meanPoint:
            count+=1
    
    print(f"{count/n*100:.3f}%")