n,m = map(int, input().split())

visit = [0]*n
result = []

def func1(idx, n, m):
    if idx == m:
        for i in result:
            print(i, end=' ')
        print()
        return

    for i in range(n):
        if visit[i] == 0:
            visit[i] = 1
            result.append(1+i)
            func1(idx+1,n,m)
            visit[i] = 0
            result.pop()

func1(0,n,m)