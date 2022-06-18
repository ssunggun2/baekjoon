import math
A,B,C=map(int,input().split())
# fixedCost=A, variCost=B, price=C, n=num

def get_break_even_point(A,B,C):
    if C>B:
        rev=(C-B)
        if float(rev).is_integer():
            n = int(A/rev)+1
            return n
        n = math.ceil(A/rev)
        return n
    else:
        return '-1'

print(get_break_even_point(A,B,C))