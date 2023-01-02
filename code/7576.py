import sys
from collections import deque
input = sys.stdin.readline

def func1():
    while(lst):
        x,y = lst.popleft()

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
            if graph[nx][ny] == 0:
                lst.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1

def func2():
    tmp1 = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                print(-1)
                return
            if graph[i][j] > tmp1:
                tmp1 = graph[i][j]
    print(tmp1-1)

    
m,n = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

lst = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            lst.append((i,j))

func1()
func2()
