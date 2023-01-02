n = int(input())
lst = [0]*(n+1)

lst[0] = 1

for i in range(3,n+1):
    if lst[i-3]:
        
        if lst[i-5]:
            lst[i] = min(lst[i-3]+1,lst[i-5]+1)
        else:
            lst[i] = lst[i-3]+1

    if lst[i-5]:
        
        if lst[i-3]:
            lst[i] = min(lst[i-3]+1,lst[i-5]+1)
        else:
            lst[i] = lst[i-5]+1


if lst[n] == 0:
    print(-1)
else:
    print(lst[n]-1)

