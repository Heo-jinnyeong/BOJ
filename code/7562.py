import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def func1(x,y):
    
    lst = deque()
    lst.append((x,y))

    while(lst):
        x,y = lst.popleft()

        if x == loc[1][0] and y == loc[1][1]:
            return

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visit[nx][ny] == 0:
                lst.append((nx,ny))
                visit[nx][ny] = visit[x][y] + 1


t = int(input())

for _ in range(t):
    n = int(input())
    loc = []
    for _ in range(2):
        loc.append(list(map(int,input().split())))

    visit = [[0]*n for _ in range(n)]

    dx = [-2,-1,1,2,2,1,-1,-2]
    dy = [1,2,2,1,-1,-2,-2,-1]

    func1(loc[0][0],loc[0][1])
    print(visit[loc[1][0]][loc[1][1]])