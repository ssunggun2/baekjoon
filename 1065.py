#어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 
#등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 
#첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.
# 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.


N = int(input())

def hansu(N):
    if N >= 100:
        hundred = N//100
        ten = (N%100)//10
        one = N%10
        if (hundred - ten) == (ten - one):
            return N
        else:
            pass
    elif 100 > N >=10:
        return N
    elif 10 > N:
        return N

hanList = []
for i in range(1, N+1):
    han=hansu(i)
    if type(han) == int:
        hanList.append(han)

print(len(hanList))