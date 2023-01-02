import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()

for i in range(m):
    tmp1 = lst[0] + lst[1]
    lst[0] = tmp1
    lst[1] = tmp1
    lst.sort()

print(sum(lst))