import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

lst = []
for i in range(n):
    tmp1 = [0]*(n+1)
    lst.append(tmp1)

lst[0][0] = graph[0][0]

for i in range(n-1):
    for j in range(len(graph[i])):
        lst[i+1][j] = max(lst[i+1][j],lst[i][j] + graph[i+1][j])
        lst[i+1][j+1] = lst[i][j] + graph[i+1][j+1]

print(max(lst[-1]))