import graphlib
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

# (w,h) (w,h+1) (w,h-1) (w+1,h-1) (w+1,h) (w+1,h+1) (w-1,h+1) (w-1,h) (w-1,h-1)
# (0,0) (0,-1) (1,-1) (1,0) (1,1) (0,1) (-1,1) (-1,0) (-1,-1)
def func1(x,y):
    if visit[x][y] == 1:
        return
    
    visit[x][y] = 1
    
    if x-1 >= 0:
        if graph[x-1][y] == 1 and visit[x-1][y] == 0:
            func1(x-1,y)
            # return
    if x+1 < b:
        if graph[x+1][y] == 1 and visit[x+1][y] == 0:
            func1(x+1,y)
            # return
    if x-1 >= 0 and y+1 < a:
        if graph[x-1][y+1] == 1 and visit[x-1][y+1] == 0:
            func1(x-1,y+1)
            # return
    if y+1 < a:
        if graph[x][y+1] == 1 and visit[x][y+1] == 0:
            func1(x,y+1)
            # return
    if x+1 < b and y+1 < a:
        if graph[x+1][y+1] == 1 and visit[x+1][y+1] == 0:
            func1(x+1,y+1)
            # return
    if x+1 < b and y-1 >= 0:
        if graph[x+1][y-1] == 1 and visit[x+1][y-1] == 0:
            func1(x+1,y-1)
            # return
    if y-1 >= 0:
        if graph[x][y-1] == 1 and visit[x][y-1] == 0:
            func1(x,y-1)
            # return
    if x-1 >= 0 and y-1 >= 0:
        if graph[x-1][y-1] == 1 and visit[x-1][y-1] == 0:
            func1(x-1,y-1)
            # return
    return


while(1):
    a,b = map(int,input().split())
    cnt = 0
    if a == 0 and b == 0:
        break

    graph = []*b
    visit = [[0 for _ in range(a)] for _ in range(b)]
    
    for i in range(b):
        graph.append(list(map(int,input().split())))
    
    for i in range(b):
        for j in range(a):
            if visit[i][j] == 0 and graph[i][j] == 1:
                func1(i,j)
                # print(visit)
                cnt += 1
            
            
    # print(graph)
    # print(visit)
    print(cnt)