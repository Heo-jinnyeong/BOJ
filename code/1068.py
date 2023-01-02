import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def func1(start):
    if visit[start] == 1:
        return
    visit[start] = 1

    if tree[start]:
        for i in tree[start]:
            func1(i)

def func2():
    cnt = 0
    for i in range(n):
        if visit[i] == 0 and len(tree[i]) == 0:
            cnt += 1
    print(cnt)

def func3():
    for i in range(m):
        for j in range(len(tree[i])):
            if len(tree[i]) == 1:
                if tree[i][j] == m:
                    tree[i].pop(j)


n = int(input())
nodes = list(map(int,input().split()))
tree = [[] for _ in range(n)]
visit = [0]*n
m = int(input())

for i in range(len(nodes)):
    if nodes[i] == -1:
        continue
    tmp1 = nodes[i]
    tree[tmp1].append(i)

# print(tree)
func1(m)
# print(visit)
func3()
# print(tree)
func2()