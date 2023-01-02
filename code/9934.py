import sys

k = int(input())
y = list(map(int, sys.stdin.readline().split()))

tree_list = [[] for _ in range(k)]

for i in range(2**(k-1)):
    tree_list[0].append(y[i*2])

print(tree_list[0])

for i in range(k):
    for j in range(2**(k-1)):
        tree_list[i].append(y[j*2])
