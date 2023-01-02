import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

x = [[] for _ in range(n+1)]
y = [0]*(n+1)

for i in range(m):
    a,b = map(int,input().split())
    x[a].append(b)
    x[b].append(a)

def func1(start):
    if y[start] == 1:
        return
    
    y[start] = 1
    
    for i in x[start]:
        func1(i)


func1(1)
print(sum(y)-1)