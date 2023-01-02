import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
x = int(input())
lst.sort()
cnt = 0

i = 0
l = i
r = i-1
while(1):
    if lst[l] >= lst[r]:
        break
    if lst[l] + lst[r] == x:
        l += 1
        r -= 1
        cnt += 1
    elif lst[l]+lst[r] < x:
        l += 1
    else:
        r -= 1


print(cnt)
