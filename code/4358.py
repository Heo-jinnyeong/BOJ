import sys
input = sys.stdin.readline

lst = {}

while(1):
    tmp1 = input().strip()
    if not tmp1:
        break
    if tmp1 in lst:
        lst[tmp1] += 1
    else:
        lst[tmp1] = 1

lst2 = sorted(lst)

sum1 = 0
for i in lst2:
    sum1 += lst[i]

for i in lst2:
    print('%s %.4f' %(i,lst[i]/sum1*100))