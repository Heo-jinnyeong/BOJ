import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def func1(start,before):
    if visit[start] != 0:
        return
    visit[start] = visit[before] + 1    
    if start == end:
        return

    for i in graph[start]:
        if visit[i] == 0:
            func1(i,start)

n = int(input())
lst_1 = []
start, end = map(int,input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visit = [0]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

func1(start,0)

if visit[end] == 0:
    print(-1)
else:
    print(visit[end]-1)