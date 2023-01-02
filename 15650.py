n,m = map(int, input().split())

list_s = []

def DFS(start):
    if len(list_s) == m:
        for i in range(m):
            print(list_s[i],end=' ')
        print()
        return

    for i in range(start,n+1):
        list_s.append(i)
        DFS(i)
        list_s.pop()

DFS(1)