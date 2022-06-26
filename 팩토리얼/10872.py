N=int(input())
z = 1
for i in range(1,N+1):
    z *= i
if N == 0:
    z= 1
print(z)