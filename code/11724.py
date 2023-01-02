import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

def func1(x):
    if visit[x] == 1:
        return
    visit[x] = 1
    for i in graph[x]:
        if visit[i] == 0:
            func1(i)
    return

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visit = [0]*(n+1)
cnt = 0 

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    if len(graph[i]) == 0:
        cnt += 1
        continue
    for j in graph[i]:
        if visit[j] == 0:
            func1(j)
            cnt += 1

print(cnt)