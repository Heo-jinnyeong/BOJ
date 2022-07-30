import sys
sys.setrecursionlimit(10**9)

n,m,v = map(int, sys.stdin.readline().split())

graph_list = [[] for _ in range(n+1)]
dfs_visit_list = [0 for i in range(n+1)]
bfs_visit_list = [0 for i in range(n+1)]
dfs_list = []
bfs_list = []
bfs_queue = []

for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph_list[a].append(b)
    graph_list[b].append(a)

def DFS(start, graph_list, visit_list):
    graph_list[start].sort()
    for i in graph_list[start]:
        if visit_list[i] == 0:
            dfs_list.append(i)
            visit_list[i] = 1
            DFS(i,graph_list,visit_list)

def BFS(start, graph_list, visit_list, bfs_queue):
    graph_list[start].sort()
    for i in graph_list[start]:
        if visit_list[i] == 0:
            bfs_list.append(i)
            visit_list[i] = 1
            bfs_queue.append(i)
    if bfs_queue:
        BFS(bfs_queue.pop(0),graph_list,visit_list,bfs_queue)
    
    


dfs_list.append(v)
dfs_visit_list[v] = 1
DFS(v,graph_list,dfs_visit_list)
for i in range(len(dfs_list)):
    print(dfs_list[i],end=' ')

print()

bfs_list.append(v)
bfs_visit_list[v] = 1
BFS(v,graph_list,bfs_visit_list,bfs_queue)
for i in range(len(bfs_list)):
    print(bfs_list[i],end=' ')