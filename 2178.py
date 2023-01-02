import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n,m = map(int,input().split())
graph = [input().strip() for i in range(n)]
visit = [[0]*m for i in range(n)]
cnt_lst = []

def func1(x,y,cnt,tmp):
    
    tmp1 = []
    for i in tmp:
        tmp1.append(i)
    
    if tmp1[x][y] == 1:
        return

    if x == (n-1) and y == (m-1):
        cnt_lst.append(cnt)
        return

    tmp1[x][y] = 1

    print(x,y,tmp1)

    if y+1 < m and graph[x][y+1] == '1':
        func1(x,y+1,cnt+1,tmp1)
    if x+1 < n and graph[x+1][y] == '1':
        func1(x+1,y,cnt+1,tmp1)
    if y-1 >= 0 and graph[x][y-1] == '1':
        func1(x,y-1,cnt+1,tmp1)
    if x-1 >= 0 and graph[x-1][y] == '1':
        func1(x-1,y,cnt+1,tmp1)

func1(0,0,1,visit)
cnt_lst.sort()
print(cnt_lst[0])
print(visit)