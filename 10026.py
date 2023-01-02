import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def func1(x,y):
    lst = deque()
    lst.append((x,y))
    visit[x][y] = 1

    while(lst):
        x,y = lst.popleft()

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visit[nx][ny] == 0 and graph[x][y] == graph[nx][ny]:
                lst.append((nx,ny))
                visit[nx][ny] = 1


n = int(input())
graph = []
lst_cnt = []
visit = [[0]*n for _ in range(n)]
for _ in range(n):
    graph.append(list(map(str,input())))

cnt = 0
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            func1(i,j)
            cnt += 1
lst_cnt.append(cnt)

cnt = 0
visit = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            func1(i,j)
            cnt += 1
lst_cnt.append(cnt)
print(lst_cnt[0],lst_cnt[1])