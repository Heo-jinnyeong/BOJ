import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
b.sort()
sum = 0

for i in range(n):
    sum += min(a)*max(b)
    a.pop(0)
    b.pop()

print(sum)