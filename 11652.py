import sys
input = sys.stdin.readline

n = int(input())
lst_1 = {}

for i in range(n):
    tmp1 = int(input())
    if tmp1 in lst_1:
        lst_1[tmp1] += 1
    else:
        lst_1[tmp1] = 1

lst_1 = sorted(lst_1.items(), key=lambda x: (-x[1],x[0]))
print(lst_1[0][0])