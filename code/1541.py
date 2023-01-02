a = input().split('-')
lst = []

for i in a:
    sum_1 = 0
    b = i.split('+')
    
    for j in b:
        sum_1 += int(j)
    lst.append(sum_1)

sum_2 = lst[0]
for i in range(1,len(lst)):
    sum_2 -= lst[i]
print(sum_2)