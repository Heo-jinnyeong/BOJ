import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    lst_1 = []
    cnt = 0
    for _ in range(n):
        a,b = map(int,input().split())
        lst_1.append([a,b])

    lst_1.sort()
    max = lst_1[0][1]
    for i in range(n):
        if lst_1[i][1] <= max:
            cnt += 1 
            max = lst_1[i][1]
    print(cnt)
