import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

dx = [-2,-1,1,2]
dy = [1,2,2,1]
visit = [0,0,0,0]

n,m = map(int,input().split())


graph = [[0 for _ in range(n)] for _ in range(m)]

def func1(x,y):
    global visit 
    graph[x][y] = 1
    for i in range(4):
        if sum(visit) == 4:
            visit = [0,0,0,0]
        if visit[i] == 1:
            continue
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= m or ny >= n:
            continue
        if graph[nx][ny] == 0:
            visit[i] = 1
            func1(nx,ny)

func1(m-1,0)
for i in graph:
    print(i)
print(visit)