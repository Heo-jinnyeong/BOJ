import sys
input = sys.stdin.readline

n,p,q = map(int,input().split())

lst = {0:1}

def func1(x):
    if x in lst:
        # print(lst[x])
        return lst[x]
    
    tmp1 = x//p
    tmp2 = x//q

    if tmp1 not in lst:
        lst[tmp1] = func1(tmp1)
    if tmp2 not in lst:
        lst[tmp2] = func1(tmp2)
    
    if tmp1 in lst and tmp2 in lst:
        x = lst[tmp1] + lst[tmp2]
        # print(x)
        return x

x = func1(n)
print(x)
