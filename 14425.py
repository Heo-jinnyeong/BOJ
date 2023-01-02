import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst_1 = []

for i in range(n):
    lst_1.append(input().strip())

cnt = 0

for i in range(m):
    tmp1 = input().strip()
    if tmp1 in lst_1:
        cnt += 1

print(cnt)