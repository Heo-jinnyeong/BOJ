n = int(input())
lst_1 = [0]*(n+1)

for i in range(2,n+1):
    lst_1[i] = lst_1[i-1]+1

    if i%2 == 0:
        lst_1[i] = min(lst_1[i],lst_1[i//2]+1)
    if i%3 == 0:
        lst_1[i] = min(lst_1[i],lst_1[i//3]+1)
print(lst_1[n])