# 실패!

a = input()
lst = {}
for i in range(len(a)):
    lst[a[i]] = 0

for i in range(len(a)):
    lst[a[i]] += 1

lst_2 = sorted(lst)

tmp1 = 1
if len(a)%2 == 0:
    for i in lst:
        if lst[i]%2 != 0:
            tmp1 = 0
            break
    if tmp1 == 0:
        print('I\'m Sorry Hansoo')
    else:
        tmp2 =[]
        for i in range(len(lst)):
            for j in range(lst[lst_2[i]]//2):
                tmp2.append(lst_2[i])
        for i in range(len(tmp2)):
            print(tmp2[i],end='')
        for i in range(len(tmp2)-1,-1,-1):
            print(tmp2[i],end='')
elif len(a)%2 == 1:
    tmp3 = 0
    for i in lst:
        if lst[i]%2 == 1:
            if tmp3 == 0:
                tmp3 = 1
            else:
                tmp3 += 1
                break
    if tmp3 > 1:
        print('I\'m Sorry Hansoo')
    else:
        for i in lst_2:
            if lst[i]%2 == 1:
                tmp4 = i

        tmp5 = []
        for i in range(len(lst)):
            if lst_2[i] == tmp4:
                continue
            for j in range(lst[lst_2[i]]//2):
                tmp5.append(lst_2[i])
        for i in range(len(tmp5)):
            print(tmp5[i],end='')
        for i in range(lst[tmp4]):
            print(tmp4,end='')
        for i in range(len(tmp5)-1,-1,-1):
            print(tmp5[i],end='')   
