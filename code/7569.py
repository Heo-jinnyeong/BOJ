from collections import deque
import sys
sys.setrecursionlimit(10**9)

def func1():
    while(lst):
        x,y,z = lst.popleft()
        visit[z][x][y] = 1

        for i in range(len(dx)):
            nx = dx[i] + x
            ny = dy[i] + y
            nz = dz[i] + z

            if nx < 0 or ny < 0 or nz < 0 or nx >= n or ny >= m or nz >= h:
                continue
            if graph[nz][nx][ny] == 0 and visit[nz][nx][ny] == 0:
                lst.append((nx,ny,nz))
                graph[nz][nx][ny] = graph[z][x][y] + 1

def func2(tmp1):
    tmp2 = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if tmp1[i][j][k] == 0:
                    print(-1)
                    return
                if tmp1[i][j][k] > tmp2:
                    tmp2 = tmp1[i][j][k]
    print(tmp2-1)


m,n,h = map(int,input().split())
graph = [[] for _ in range(h)]
for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int,input().split())))

visit = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]

# 위 아래 12 3 6 9
dx = [0,0,-1,0,1,0]
dy = [0,0,0,1,0,-1]
dz = [1,-1,0,0,0,0]

lst = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                lst.append((j,k,i))

func1()
func2(graph)