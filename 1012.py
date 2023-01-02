import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def func1(y,x):
    global cnt
    
    if visit[y][x] == 1:
        return
    visit[y][x] = 1
    
    if y+1 < n and graph[y+1][x] == 1 and visit[y+1][x] == 0:
        func1(y+1,x)
        return
    if x+1 < m and graph[y][x+1] == 1 and visit[y][x+1] == 0:
        func1(y,x+1)
        return
    if y-1 >= 0 and graph[y-1][x] == 1 and visit[y-1][x] == 0:
        func1(y-1,x)
        return
    if x-1 >= 0 and graph[y][x-1] == 1 and visit[y][x-1] == 0:
        func1(y,x-1)
        return
    cnt += 1
    


t = int(input())

for _ in range(t):
    m,n,k = map(int,input().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    visit = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0
    


    for i in range(k):
        a,b = map(int,input().split())
        graph[b][a] = 1
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                func1(i,j)

    print(cnt)

    print(visit)
