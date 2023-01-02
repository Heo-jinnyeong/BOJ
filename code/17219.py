import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst1 = {}
lst2 = []

for _ in range(n):
    tmp1,tmp2 = input().strip().split()
    lst1[tmp1] = tmp2

for _ in range(m):
    lst2.append(input().strip())

for i in lst2:
    print(lst1[i])