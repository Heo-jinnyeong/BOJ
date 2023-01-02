import sys
input = sys.stdin.readline

r,c = map(int,input().split())

graph = []
visit = [0]*26
lst = []

for _ in range(r):
    graph.append(list(input().strip()))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def func1(x,y,z):
    global lst
    global cnt
    cnt = max(cnt,z)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= r or ny >= c:
            continue
        if visit[ord(graph[nx][ny])-65] == 0:
            visit[ord(graph[nx][ny])-65] = 1
            func1(nx,ny,z+1)
            visit[ord(graph[nx][ny])-65] = 0
cnt = 1
visit[ord(graph[0][0])-65] = 1
func1(0,0,cnt)   
print(cnt)
