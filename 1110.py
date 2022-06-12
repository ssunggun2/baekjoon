N = int(input())
M=N
count = 0
def getNew(N):
    a=N//10
    b=N%10
    c=(a+b)%10
    N=b*10+c
    return N

while True:
    M=getNew(M)
    count+=1
    if M==N:
        break
    
print(count)