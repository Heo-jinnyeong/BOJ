# 1

# import sys
# sys.setrecursionlimit(10**9)
# input = sys.stdin.readline

# n = int(input())
# graph = []
# visit = [[0 for _ in range(n)] for _ in range(n)]
# cnt_lst = []

# for _ in range(n):
#     graph.append(input().strip())

# def func1(x,y):
#     if visit[x][y] == 1:
#         return
    
#     visit[x][y] = 1

#     if y+1 < n and graph[x][y+1] == '1':
#         func1(x,y+1)
#     if x+1 < n and graph[x+1][y] == '1':
#         func1(x+1,y)
#     if y-1 >= 0 and graph[x][y-1] == '1':
#         func1(x,y-1)
#     if x-1 >= 0  and graph[x-1][y] == '1':
#         func1(x-1,y)
    
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == '1' and visit[i][j] == 0:
#             func1(i,j)
#             tmp1 = 0
#             for i in range(n):
#                 tmp1 += sum(visit[i])
#             cnt_lst.append(tmp1 - sum(cnt_lst))

# cnt_lst.sort()
# print(len(cnt_lst))
# if len(cnt_lst) == 0:
#     print(0)
# for i in cnt_lst:
#     print(i)

# 2
import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input().strip())))

def func1(x,y):
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    lst = deque()
    lst.append((x,y))
    graph[x][y] = 0
    cnt = 1

    while(lst):
        x,y = lst.popleft()

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= n or ny >= n or nx < 0 or ny < 0:
                continue
            if graph[nx][ny] == 1:
                lst.append((nx,ny))
                graph[nx][ny] = 0
                cnt += 1
    return cnt

cnt_lst = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt_lst.append(func1(i,j))

cnt_lst.sort()
print(len(cnt_lst))
for i in cnt_lst:
    print(i)