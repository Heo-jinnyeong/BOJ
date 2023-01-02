import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def func1(x,y):
    global cnt
    if x == (m-1) and y == (n-1):
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    way = 0
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= m or ny >= n:
            continue
        if graph[nx][ny] < graph[x][y]: 
            way += func1(nx,ny)
    dp[x][y] = way
    return dp[x][y]

m,n = map(int,input().split())
graph = []
for i in range(m):
    graph.append(list(map(int,input().split())))

dp = [[-1]*n for _ in range(m)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

cnt = 0
print(func1(0,0))
