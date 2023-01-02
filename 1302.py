import sys
input = sys.stdin.readline

n = int(input())
lst = {}

for i in range(n):
    tmp1 = input().strip()
    if tmp1 in lst:
        lst[tmp1] += 1
    else:
        lst[tmp1] = 1

lst = sorted(lst.items(), key=lambda x: (-x[1],x[0]))

i = 0
tmp2 = 0
while(1):
    if lst[i][1] == lst[i+1][1]:
        tmp2 = i+1
    else:
        break

lst = lst[:tmp2+1]
lst = sorted(lst)
print(lst[0][0])