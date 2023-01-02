# fail !!

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n = int(input())
lst = [[] for _ in range(n)]
visit = [[0]*n for _ in range(n)]

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            lst[i].append(j)
            lst[j].append(i)



def func1(start,x,y):
    if x != start:
        graph[x][start] = 1

    if start == y:
        graph[y][x] = 1
        return

    graph[x][y] = 1
    graph[y][x] = 1

    for i in graph[y]:
        if x == i:
            continue
        graph[y][i] = 1
        func1(x,i,y)

    
func1(0,0,1)
print(graph)



