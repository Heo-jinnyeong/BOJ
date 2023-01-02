import sys
import copy
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

max_rain = max(max(graph))

def func1(x,y,z,h):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    lst = deque()
    lst.append((x,y))
    z[x][y] = 1
    

    while(lst):
        x,y = lst.popleft()
        
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] > h and z[nx][ny] == 0:
                lst.append((nx,ny))
                z[nx][ny] = 1

    
    return

cnt_lst = []
for i in range(max_rain+1):
    
    visit = [[0]*n for _ in range(n)]
    
    cnt = 0
    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visit[j][k] == 0:
                func1(j,k,visit,i)
                cnt += 1
    cnt_lst.append(cnt)
    
print(max(cnt_lst))

# import sys
# from collections import deque
# sys.setrecursionlimit(10**9)
# input = sys.stdin.readline

# n = int(input())
# graph = [list(map(int,input().split()))]

