import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

m,n,k = map(int,input().split())

def func1(x1,y1,x2,y2):
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j] = 1

def func2(x,y):
    visit[y][x] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or ny >= m or nx >= n:
            continue
        if graph[ny][nx] == 0 and visit[ny][nx] == 0:
            lst.append([ny,nx])
            func2(nx,ny)

graph = [[0]*n for _ in range(m)]

for i in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    func1(x1,y1,x2,y2)

visit = [[0]*n for _ in range(m)]
lst = []
lst1 = []

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0 and visit[i][j] == 0:
            func2(j,i)
            lst1.append(len(lst)+1)
            lst = []
            
lst1.sort()
print(len(lst1))
for i in lst1:
    print(i,end=' ')
