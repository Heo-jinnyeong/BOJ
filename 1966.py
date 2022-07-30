import sys


a = int(input())

for i in range(a):
    
    n,m = map(int, input().split())
    x = list(map(int, sys.stdin.readline().split()))

    y = [0 for i in range(n)]
    y[m] = 1
    cnt = 0

    while(1):  
        if x[0] == max(x):
            if y[0] == 1:
                cnt += 1
                print(cnt)
                break
            else:
                cnt += 1
                x.pop(0)
                y.pop(0)

        else:
            x.append(x.pop(0))
            y.append(y.pop(0))