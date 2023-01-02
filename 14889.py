import sys
input = sys.stdin.readline

def DFS(level, start):
    global min_diff
    if level == n//2:
                
        sum_a = 0
        sum_b = 0
        
        for i in range(n):
            for j in range(n):
                if visit[i] and visit[j]:
                    sum_a += lst[i][j]
                elif not visit[i] and not visit[j]:
                    sum_b += lst[i][j]
        min_diff = min(min_diff, abs(sum_a-sum_b))
        return

    for i in range(start, n):
        if not visit[i]:
            visit[i] = 1
            DFS(level+1,i+1)
            visit[i] = 0

n = int(input())

visit = [0 for _ in range(n)]

lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

min_diff = int(1e9)

DFS(0,0)
print(min_diff)